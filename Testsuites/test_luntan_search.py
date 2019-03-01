import unittest
from Testsuites.Base_testcase import Base_testcase
from Pageobjects.luntan_homepage_one import Luntan_one
class LuntanSearch_one(Base_testcase):
    def test_ltone(self):
        l=Luntan_one(self.driver)
        l.get("http://127.0.0.1/forum.php")
        l.denglu_yonghu("admin")
        l.denglu_mima("admin")
        l.denglu()
        l.shuijiao(3)
        l.jinru_fatie()
        l.fatie_biaoti("admin发帖啦")
        l.qiehuan()
        l.fatie_neirong("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        l.dangqian()
        l.fatiequeding()
        l.shuijiao(3)
        l.huitie_neirong("这是我的回帖！！！")
        l.huitie_queding()
        l.tuichu()

if __name__=='__main__':
    unittest.main()