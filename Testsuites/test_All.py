import unittest
import HTMLTestRunner
import os
import sys
sys.path.append("C:\\Users\\lenovo203\\PycharmProjects\\untitled1\\")
dir='./'
# c_path=os.path.dirname(os.path.realpath(__file__))
c_path=os.path.dirname(os.path.abspath('.'))
report_path=os.path.join(c_path,'report')
if not os.path.exists(report_path): os.mkdir(report_path)
sut=unittest.TestLoader().discover(dir,pattern='test_luntan_*')
if __name__=='__main__':
    html_report=report_path+r'\result.html'
    fp=open(html_report,'wb')
    r=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告1",description="用例执行情况1")
    r.run(sut)

# import unittest
# import HTMLTestRunner
# import os
# from Testsuites.test_luntan_search import LuntanSearch_one
# from Testsuites.test_luntan_search_t import LuntanSearch_two
# from Testsuites.test_luntan_search_hree import LuntanSearch_three
#
# c_path=os.path.dirname(os.path.realpath(__file__))
# report_path=os.path.join(c_path,'report')
# if not os.path.exists(report_path): os.mkdir(report_path)
#
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(LuntanSearch_one))
# suite.addTest(unittest.makeSuite(LuntanSearch_two))
# suite.addTest(unittest.makeSuite(LuntanSearch_three))
# if __name__=='__main__':
#     html_report=report_path+r'\result.html'
#     fp=open(html_report,'wb')
#     r=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
#     r.run(suite)