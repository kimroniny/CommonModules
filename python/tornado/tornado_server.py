# -*- coding: utf-8 -*-
import argparse
import sys
import traceback
import datetime
import time
import json, random
import os

import tornado
import tornado.httpserver, tornado.ioloop, tornado.options
import tornado.httpclient, tornado.web, tornado.gen

class Api(tornado.web.RequestHandler):

    def initialize(self, args):
        """
        每次有请求过来，都会运行该函数
        """
        pass

    def get(self, *args, **kwargs):
        pass
        

    def post(self, *args, **kwargs):
        pass


def make_app(args):
    return tornado.web.Application([
        (r"/api/(.*)", Api, dict(args=args)),
    ])

def getArg():
    parser = argparse.ArgumentParser(description='params for python')
    parser.add_argument('--port', type=int, default=10051)
    parser.add_argument('--start_num', type=int, default=1)
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

