# -*- coding: utf8 -*-
import os, sys, unittest, cv2, random, time

import grpc_server as entry
global args
args = ['--port', '10051', '--max_workers', '10']
old_sys_argv = sys.argv
sys.argv = [old_sys_argv[0]] + args
args = entry.getArg()
os.environ['CUDA_VISIBLE_DEVICES'] = str(args.gpu_devs)

from proto import grpc_pb2, grpc_pb2_grpc
from concurrent import futures
import grpc
import soundfile as sf
import numpy as np
import HtmlTestRunner

class AudioClassificationTest(unittest.TestCase):
    def setUp(self):
        options = [('grpc.max_send_message_length', 1000 * 1024 * 1024 * 2),
                   ('grpc.max_receive_message_length', 1000 * 1024 * 1024 * 2)]
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.max_workers), options=options)
        grpc_pb2_grpc.add_GreeterServicer_to_server(entry.Greeter(), self.server)
        self.server.add_insecure_port('[::]:%d' % args.port)
        self.server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。

    def tearDown(self):
        self.server.stop(0)

    def test_video_check(self):
        # 这里也是grpc client的写法
        with grpc.insecure_channel('localhost:10051') as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)
            audio_path = ''
            image_fp_list, sr = sf.read(audio_path, dtype='int16')
            shape = image_fp_list.shape
            req = grpc_pb2.VideoRequest(
                vid=str(int(time.time()))+''.join(random.choice('abcdef') for _ in range(8)),
                mage_fp_list=grpc_pb2.nplist(
                    body=image_fp_list.tobytes(),
                    shape=grpc_pb2.npshape(x=shape[0]),
                    dtype=image_fp_list.dtype.name
                ),
                rate=sr,
                max_length=2,
                detect_type=0
            )
            rep = stub.audio_classify(req)
            nplist = rep.score_list
            body, dtype, shape = nplist.body, nplist.dtype, nplist.shape
            result_list = np.frombuffer(body, dtype).reshape(shape.x, shape.y)
            print(result_list)

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(
            report_title='ball_check_server Test',
            report_name='ball_check_server'
        )
    itersuite = unittest.TestLoader().loadTestsFromTestCase(AudioClassificationTest)
    runner.run(itersuite)
