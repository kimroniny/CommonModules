import unittest
import coverage

class TestMain(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def testhello(self):
        self.assertTrue(True)

    def tearDown(self):
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
    