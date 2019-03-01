import unittest
from Testsuites.Base_testcase import Base_testcase
from Pageobjects.luntan_homepage_one import Luntan_one
class LuntanSearch_three(Base_testcase):
    def test_ltthree(self):
        l=Luntan_one(self.driver)
        l.get("http://127.0.0.1/forum.php")
        l.denglu_yonghu("admin")
        l.denglu_mima("admin")
        l.denglu()
        l.shuijiao(3)
        t=["qwer"]
        jg=l.jinrusousuo(t[0])
        # assert jg in t[0]
        print("匹配正确")
        self.assertEqual(jg,t[0],msg=jg)
        l.shuijiao(2)
        l.tuichu()
if __name__=='__main__':
    unittest.main(verbosity=2)