#-*- coding:UTF-8 -*-
import HTMLTestRunner
import  unittest
class baidu(unittest.TestCase):
    @classmethod
    def setUp(self):
        print 'there is first '
    def test_1(self):
        print '111'
    def test_2(self):
        print '2222'
    def test_3(self):
        print '3333'
    def test_4(self):
        print '4444'
    def tearDown(self):
        print 'endless'

if __name__ == '__main__':

    filename=r"C:\Users\shasha.yan\PycharmProjects\test1\sendgift\case.html"
    fp=file(filename,"wb")
    runer=HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动测试 ",description=u"测试结果")
    testsuite=unittest.makeSuite(baidu)
    runer.run(testsuite)
    fp.close()