from Pageobjects.base import BasePage
from selenium.webdriver.common.by import By
class Luntan_one(BasePage):
    zcmima = 0
    l_name_input=(By.NAME,'username')      #输入   thread_subject
    l_password_input=(By.NAME,'password')
    l_ftbiaoti_input=(By.NAME,'subject')
    l_ftneirong_input=(By.TAG_NAME,'body')
    l_huifu_input=(By.NAME,'message')     #回复
    l_tianjiabank_input=(By.CSS_SELECTOR,'.tb :nth-last-child(2) :nth-last-child(2) .board .txt')
    #搜索框
    l_sousuo_input=(By.ID,'scbar_txt')
    #帖子主题
    l_tiezizhuti=(By.ID,'thread_subject')

    l_button_denglu=(By.TAG_NAME,'button')      #click
    l_button_jinrufatie=(By.CSS_SELECTOR,'.bm_c h2 a')
    l_button_fatie=(By.ID,'newspecial')
    l_button_toupiao=(By.PARTIAL_LINK_TEXT,'发起投票')             #发帖按钮
    l_button_tijiaoft=(By.ID,'postsubmit')           ##这里这里
    l_button_tijiaohf=(By.ID,'fastpostsubmit')
    l_button_tuichu=(By.PARTIAL_LINK_TEXT,'退出')
    l_button_guanlizhongxin=(By.PARTIAL_LINK_TEXT,'管理中心')
    l_button_luntan=(By.PARTIAL_LINK_TEXT,'论坛')
    l_button_tianjiaxinbank=(By.CSS_SELECTOR,'.lastboard a')
    l_button_bktijiao=(By.NAME,'editsubmit')
    l_button_jinruxinbank=(By.CSS_SELECTOR,'.fl_tb :nth-last-child(2) .fl_icn ')   #想要进入新板块
    l_button_danxuankuang=(By.CSS_SELECTOR,'.bm_c :nth-child(2) :nth-child(2) ')   #获取单选按钮
    l_button_shantie=(By.PARTIAL_LINK_TEXT,"删除")                                 #删除帖子按钮
    l_button_shanchuqueding=(By.ID,'modsubmit')                                    #删除确定
    l_button_djsousuo=(By.NAME,'searchsubmit')                                     #点击搜索
    l_quedingtoupiao=(By.NAME,"pollsubmit")            #确定投票

    #l_button_sousuojg=(By.LINK_TEXT,'')    # 搜索结果连接

    l_qiehuan_one=(By.TAG_NAME,'iframe')

    l_huoquwenb=(By.ID,'thread_subject')

    #三个搜索框写死
    l_sousuokuang_one=(By.XPATH,'//*[@id="pollm_c_1"]/p[1]/input')
    l_sousuokuang_two=(By.XPATH,'//*[@id="pollm_c_1"]/p[2]/input')
    l_sousuokuang_three=(By.XPATH,'//*[@id="pollm_c_1"]/p[3]/input')

    def denglu_yonghu(self,text):
        self.sendkeys(text,*self.l_name_input)
    def denglu_mima(self,text):
        self.sendkeys(text, *self.l_password_input)
    def denglu(self):
        self.click(*self.l_button_denglu)
        ###
    def jinru_fatie(self):
        self.click(*self.l_button_jinrufatie)
        self.click(*self.l_button_fatie)
        ###
    def fatie_biaoti(self,text):
        self.sendkeys(text,*self.l_ftbiaoti_input)

    def qiehuan(self):
        self.switch_to(*self.l_qiehuan_one)

    def fatie_neirong(self,text):
        self.sendkeys(text,*self.l_ftneirong_input)
    def dangqian(self):
        self.switch_dangqian()
    def fatiequeding(self):
        self.click(*self.l_button_tijiaoft)
    def huitie_neirong(self,text):
        self.sendkeys(text,*self.l_huifu_input)
    def huitie_queding(self):
        self.click(*self.l_button_tijiaohf)
    def tuichu(self):
        self.click(*self.l_button_tuichu)
#########################################################
    def jinrubank(self):         #进入办款

        self.click(*self.l_button_guanlizhongxin)
        self.qieyemian(1)
        self.panduan("admin")
        self.click(*self.l_button_luntan)
        self.qiehuan()
    def tianjiaxinbk(self):
        self.click(*self.l_button_tianjiaxinbank)
    def bkname(self,text):
        self.sendkeys(text,*self.l_tianjiabank_input)
###想要进入新板块
    def jinruxinbk(self):
        self.click(*self.l_button_jinruxinbank)
        self.click(*self.l_button_fatie)

    def shanchutiezi(self):
        self.click(*self.l_button_jinrufatie)
        self.click(*self.l_button_danxuankuang)
        self.click(*self.l_button_shantie)
        self.click(*self.l_button_shanchuqueding)

    def dandufatie(self):
        self.click(*self.l_button_fatie)

    def xinbankuaitijiao(self):
        self.click(*self.l_button_bktijiao)               #提交新板块
    def qingchu(self):
        self.clear(*self.l_tianjiabank_input)             #清除页面元素

    def jinrusousuo(self,text):
        self.sendkeys(text,*self.l_sousuo_input)
        self.click(*self.l_button_djsousuo)                 #点击搜索
        self.l_button_sousuojg=(By.PARTIAL_LINK_TEXT,text)          #获取结果链接元素
        self.qieyemian(1)
        self.click(*self.l_button_sousuojg)
        self.qieyemian(2)
        t=self.hqtext(*self.l_tiezizhuti)
        return t

    def jinru_toupiao(self):
        self.click(*self.l_button_jinrufatie)
        self.click(*self.l_button_fatie)
        self.click(*self.l_button_toupiao)
    def sousuokuangshuru(self,text1,text2,text3):
        self.sendkeys(text1,*self.l_sousuokuang_one)
        self.sendkeys(text2, *self.l_sousuokuang_two)
        self.sendkeys(text3, *self.l_sousuokuang_three)
    def xuanze(self,n):
        self.xuanzekuang=(By.ID,"option_"+n+"")
        self.click(*self.xuanzekuang)

    def huodesuoyou(self):
        '''

        the li you title and people

        '''
        list1=[]
        self.diyigebiaoti=(By.CSS_SELECTOR,'.pcht :first-of-type .pvt')
        self.diyigerenshu=(By.CSS_SELECTOR,'.pcht :nth-child(2) :nth-child(2)')

        self.diergebiaoti=(By.CSS_SELECTOR,'.pcht :nth-child(3) .pvt')
        self.diergerenshu=(By.CSS_SELECTOR,'.pcht :nth-child(4) :nth-child(2)')

        self.disangebiaoti=(By.CSS_SELECTOR,'.pcht :nth-child(5) .pvt')
        self.disangerenshu=(By.CSS_SELECTOR,'.pcht :nth-child(6) :nth-child(2)')

        list1.append(self.hqtext(*self.diyigebiaoti))
        list1.append(self.hqtext(*self.diyigerenshu))
        list1.append(self.hqtext(*self.diergebiaoti))
        list1.append(self.hqtext(*self.diergerenshu))
        list1.append(self.hqtext(*self.disangebiaoti))
        list1.append(self.hqtext(*self.disangerenshu))
        return list1
    def huodezt(self):
        zt=self.hqtext(*self.l_tiezizhuti)
        return zt
    def tijiaotoupiao(self):
        self.click(*self.l_quedingtoupiao)

    def panduan(self,text):
        try:
            self.zcmima = (By.NAME, 'admin_password')
            self.queding = (By.NAME, "submit")
            if self.zcmima:
                self.sendkeys(text,*self.zcmima)
                self.click(*self.queding)
        except Exception as e:
            print("这里没找见，继续下一步：",e)
