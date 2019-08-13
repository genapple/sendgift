import  unittest
#-*- coding:UTF-8 -*-
#from selenium import  webdriver
import HTMLTestRunner
class learn(unittest.TestCase):
    def test_1(self):

        print "sssss"
    def test_a(self):
        print ("2")
    def test_A(self):
        print ("3")
    def test_B(self):
        print ("4")
    def test_C(self):
        print ("5")
# if __name__ == '__main__':
#     print 'kkkkkk'
#     testsuite=unittest.makeSuite(learn)
#     #testsuite=unittest.TestSuite()
#     #testsuite.addTests(learn)
#     print 'ddddd'
#     filename="C:\\Users\\shasha.yan\\PycharmProjects\\test1\\sendgift\\result.html"
#     fp=open(filename,"wb")
#     print 'qqqqq'
#     runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"aa", description=u"bb")
#     runner.run(testsuite)
#     fp.close()
