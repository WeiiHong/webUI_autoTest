import unittest
from Testsuites.Base_testcase import Base_testcase
from Pageobjects.baidu_homepage import HomePage

class BaiduSearch(Base_testcase):

    def test_baidu(self):
        h=HomePage(self.driver)
        h.get("https://www.baidu.com")
        h.shuru("地下城与勇士")
        h.shuijiao(3)

if __name__=='__main__':
    unittest.main()
