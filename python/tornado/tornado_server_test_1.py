# -*- coding: utf-8 -*-
import os, sys, json, time, random, urllib
project_dir = os.path.dirname(os.path.abspath(os.path.curdir))
sys.path.append(
    project_dir
)
sys.path.append(
    os.path.join(project_dir, 'lib')
)
print(sys.path)


# import unittest, requests, mimetypes
import tornado_server as entry
# import asr_server.http_get_info as
from functools import partial
from uuid import uuid4
import tornado.ioloop
import unittest
import mimetypes

import tornado.httpclient
import tornado.ioloop
from tornado.testing import *

'''
POST / HTTP/1.1
Host: localhost:8000
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------8721656041911415653955004498
Content-Length: 465

-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myTextField"

Test
-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myCheckBox"

on
-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myFile"; filename="test.txt"
Content-Type: text/plain

Simple file.
-----------------------------8721656041911415653955004498--
'''

@gen.coroutine
def multipart_producer(boundary, keyname, filenames, params, write):
    boundary_bytes = boundary.encode()

    for filename in filenames:
        filename_bytes = filename.encode()
        mtype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        buf = (
            (b"--%s\r\n" % boundary_bytes)
            + (
                b'Content-Disposition: form-data; name="%s"; filename="%s"\r\n'
                % (keyname.encode(), filename_bytes)
            )
            + (b"Content-Type: %s\r\n" % mtype.encode())
            + b"\r\n"
        )
        yield write(buf)
        with open(filename, "rb") as f:
            while True:
                # 16k at a time.
                chunk = f.read(16 * 1024)
                if not chunk:
                    break
                yield write(chunk)

        yield write(b"\r\n")
    for k, v in params.items():
        buf = (
                (b"--%s\r\n" % boundary_bytes)
                + (
                        b'Content-Disposition: form-data; name="%s"\r\n'
                        % (k.encode())
                )
                + b"\r\n"
        )
        yield write(buf)
        yield write(v.encode())
        yield write(b"\r\n")

    yield write(b"--%s--\r\n" % (boundary_bytes,))

class Badmusictest(AsyncHTTPTestCase):
    def setUp(self):
        super(Badmusictest, self).setUp()


    def get_app(self):
        # 设置参数
        self.port, self.start_num = "7894", 11
        args = ['--port', self.port, '--start_num', str(self.start_num)]
        old_sys_argv = sys.argv
        sys.argv = [old_sys_argv[0]] + args
        self.args = entry.getArg()
        return entry.make_app(self.args)

    def test_getArg(self):
        args = entry.getArg()
        self.assertEqual(args.port, self.port)
        self.assertEqual(args.start_num, self.start_num)

    def test_checkMusicHandler_POST(self):
        url = '/checkbadmusic'
        boundary = uuid4().hex
        headers = {"Content-Type": "multipart/form-data; boundary=%s" % boundary}
        params = {'vid': str(int(time.time()))+''.join(random.choice('abcdef') for _ in range(8))}
        producer = partial(multipart_producer, boundary, 'sound', ['test.wav'], params)
        response = self.fetch(
            path=url,
            method="POST",
            headers=headers,
            body_producer=producer,
        )
        self.assertEqual(response.code, 200)
        res = json.loads(response.body)
        self.assertEqual(res['error'], '')

    def test_checkMusicHandler_GET(self):
        url = '/checkbadmusic'
        params = {
            'vid': str(int(time.time()))+''.join(random.choice('abcdef') for _ in range(8)),
            'sound_url': 'https://file-examples.com/wp-content/uploads/2017/11/file_example_WAV_2MG.wav',
        }
        response = self.fetch(
            path=url,
            body=urllib.urlencode(params)
        )
        self.assertEqual(response.code, 200)

import HtmlTestRunner

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Badmusic Test',
            report_name='BadMusic'
        )
    itersuite = unittest.TestLoader().loadTestsFromTestCase(Badmusictest)
    runner.run(itersuite)
