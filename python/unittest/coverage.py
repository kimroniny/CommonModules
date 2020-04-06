import unittest
import coverage

class TestMain(unittest.TestCase):
    def testhello(self):
        # cov = coverage.Coverage()
        # cov.start()
        self.assertTrue(True)
        # cov.stop()
        # cov.save()
        # cov.report()

if __name__ == '__main__':
    """
    如果要在__main__中写coverage，就得按照这种形式，不能使用 unittest.main()
    如果要在测试用例中写，就随意了
    """
    runner = unittest.TextTestRunner()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)

    cov = coverage.Coverage()
    cov.start()
    runner.run(suite)
    cov.stop()
    cov.save()
    cov.report()
    