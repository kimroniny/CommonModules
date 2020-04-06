# encoding=utf-8
import multiprocessing
import socket
import sys
import time
import traceback
from concurrent import futures

import grpc
import numpy as np

from proto import grpc_pb2, grpc_pb2_grpc

import argparse, os
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# /usr/local/qqwebsrv/python/bin/python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./hello.proto
def getArg():
    parser = argparse.ArgumentParser(description='params for python')
    parser.add_argument('--port', type=int, default=10051)
    parser.add_argument('--max_workers', type=int, default=10)
    parser.add_argument('--start_num', type=int, default=2)

    return parser.parse_args()

class Greeter(audio_pb2_grpc.GreeterServicer):
    # 工作函数
    def audio_classify(self, request, context):
        result_score_array = np.array([])
        try:
            pass
        except Exception as e:
            print(traceback.format_exc())
        finally:
            return grpc_pb2.VideoReply(
                score_list=grpc_pb2.nplist(
                    body=result_score_array.tobytes(),
                    shape=grpc_pb2.npshape(x=result_score_array.shape[0], y=result_score_array.shape[1]),
                    dtype=str(result_score_array.dtype),
                )
            )


def serve(bind_address=None):
    # gRPC 服务器
    # grpc 参数设置 https://grpc.github.io/grpc/core/group__grpc__arg__keys.html
    options = [('grpc.max_send_message_length', 1000 * 1024 * 1024),
               ('grpc.max_receive_message_length', 1000 * 1024 * 1024),('grpc.so_reuseport', 1)]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.max_workers), options=options)
    grpc_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    if bind_address is None:
        server.add_insecure_port('[::]:%d' % args.port)
    else:
        server.add_insecure_port(bind_address)
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

def runserverth():
    self_ip = get_host_ip()
    port = args.port
    bind_address = '{}:{}'.format(self_ip,port)
    print ("Binding to '%s'", bind_address)
    sys.stdout.flush() #刷新stdout，这样就能每隔一秒输出一个数字
    workers = []
    for _ in range(args.start_num):
        worker = multiprocessing.Process(target=serve, args=(bind_address,))
        workers.append(worker)
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

if __name__ == '__main__':
    date = time.strftime("%Y%m%d", time.localtime())
    args = getArg()
    print("args.port:%d" % args.port)
    runserverth()
    # serve()