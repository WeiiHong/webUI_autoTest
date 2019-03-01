import unittest
from Testsuites.Base_testcase import Base_testcase
from Pageobjects.luntan_homepage_one import Luntan_one
class LuntanSearch_fore(Base_testcase):
    def test_ltfore(self):
        l=Luntan_one(self.driver)
        l.get("http://127.0.0.1/forum.php")
        l.denglu_yonghu("admin")
        l.denglu_mima("admin")
        l.denglu()
        l.shuijiao(3)

        l.jinru_toupiao()
        l.fatie_biaoti("我的投票")

        l.sousuokuangshuru("我的第一个问题","第二个问题","第三个问题")
        l.fatiequeding()
        l.shuijiao(5)

        l.xuanze('2')
        l.tijiaotoupiao()

        list1=l.huodesuoyou()
        for i in range(0,len(list1)):
            if i%2==0:
                print("题目是：",list1[i],"；投票人数是：",list1[i+1])
        zhuti=l.huodezt()
        print("主题是：",zhuti)
        l.shuijiao(2)

if __name__=='__main__':
    unittest.main()