import HtmlTestRunner
import unittest

class TestMain(unittest.TestCase):
    def testhello(self):
        # cov = coverage.Coverage()
        # cov.start()
        self.assertTrue(True)
        # cov.stop()
        # cov.save()
        # cov.report()

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Unit Test',
            report_name='class TestMain'
        )
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestMain)
    runner.run(itersuite)