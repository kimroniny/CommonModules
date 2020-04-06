import unittest,requests
import noise_detect.noise_video_detect_class as noise_video_detect_class
import audio_embedding_http_server as audio_embedding_http_server
from tornado.testing import AsyncHTTPTestCase
import json


class TestMain(AsyncHTTPTestCase):

    def get_app(self):
        args = audio_embedding_http_server.getArg()
        return audio_embedding_http_server.make_app(args)
    
    def test_main(self):
        #self.http_client.fetch('/post_server',self.stop())
        #response = self.wait()
        #print(response)
        image_files ="./test/a3041fdpxhz.wav"
        files = {"sound": open(image_files, 'rb')}
        data = {}
        a = requests.Request(url="http://localhost/test", files=files, data=data)
        prepare = a.prepare()
        content_type = prepare.headers.get('Content-Type')
        body = prepare.body
        headers = {
            "Content-Type": content_type,
        }
        response = self.fetch('/post_server',method="POST",body=body,headers=headers)
        #print(response.body)
        #print(response)
        info = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(info['code'], 0)
        self.assertEqual(len(info['check_result']),128)
        
if __name__ == '__main__':
    import comm_log.comm_log as comm_log
    comm_log.init(str(__file__).split(".")[0])
    unittest.main()