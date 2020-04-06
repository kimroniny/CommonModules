# -*- coding: utf-8 -*-
import argparse
import sys
import traceback
import datetime
import time
import json, random
import os, redis, MySQLdb

import tornado
import tornado.httpserver, tornado.ioloop, tornado.options
import tornado.httpclient, tornado.web, tornado.gen

def try_json_loads(body):
    try:
        res = json.loads(body)
    except Exception as e:
        print(traceback.format_exc())
        res = {}
    finally:
        return res

class audio_class_detect(tornado.web.RequestHandler):

    def initialize(self, args):
        """
        每次有请求过来，都会运行该函数
        """
        pass

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        try:
            # self.request.arguments
            # self.request.body
            # self.request.body_arguments
            # self.request.query
            # self.request.query_arguments
            request_data = try_json_loads(self.request.body)
            print("callback receive: {}".format(request_data))
            self.write("success")
        except Exception as e:
            print (traceback.format_exc())
            self.write("fail")


def make_app(args):
    return tornado.web.Application([
        (r"/callback_url", audio_class_detect, dict(args=args)),
    ])

def getArg():
    parser = argparse.ArgumentParser(description='params for python')
    parser.add_argument('--port', type=int, default=10051)
    parser.add_argument('--start_num', type=int, default=2)
    parser.add_argument('--redis_name', type=str, default="")
    parser.add_argument('--redis_key', type=str, default="callback_data")
    return parser.parse_args()

if __name__ == "__main__":
    args = getArg()
    try:
        app = make_app(args)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.bind(args.port)
        http_server.start(args.start_num)
        tornado.ioloop.IOLoop.instance().start()
        time.sleep(1)
    except Exception as e:
        print (traceback.format_exc())

