import unittest
from Testsuites.Base_testcase import Base_testcase
from Pageobjects.luntan_homepage_one import Luntan_one
class LuntanSearch_two(Base_testcase):
    def test_lttwo(self):
        '''
        add bankuai
        '''
        l=Luntan_one(self.driver)
        l.get("http://127.0.0.1/forum.php")
        l.denglu_yonghu("admin")
        l.denglu_mima("admin")
        l.denglu()
        l.shuijiao(2)

        l.shanchutiezi()

        l.jinrubank()
        l.shuijiao(3)

        l.tianjiaxinbk()
        l.qingchu()
        l.bkname("wxwxwx")    #添加新板块完成
        l.xinbankuaitijiao()

        l.shuijiao(2)
        l.qieyemian(1)

        l.tuichu()
        l.tuichu()
        l.shuijiao(3)
        l.denglu_yonghu("weihong")
        l.denglu_mima("weihong")
        l.denglu()

        l.shuijiao(3)

        l.jinruxinbk()    #进入最后一个版块

        l.fatie_biaoti("我是weih")
        l.qieyemian(1)
        l.qiehuan()
        l.fatie_neirong("11111111111111bbaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        l.qieyemian(1)
        l.fatiequeding()
        l.shuijiao(2)
        l.huitie_neirong("11111111111111这是我的回帖！！！")
        l.shuijiao(15)
        l.huitie_queding()
        l.shuijiao(2)
if __name__=='__main__':
    unittest.main()
