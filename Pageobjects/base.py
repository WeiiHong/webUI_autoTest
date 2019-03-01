from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from framework.logger import Logger
import time
logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.a=self.driver.current_window_handle
    def back(self):
        self.driver.back()
    def get(self,url):
        self.driver.get(url)
        logger.info("进入网址")
    def find_element(self,*loc):
        '''
        find element

        '''
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        logger.info("成功找到元素")
        return self.driver.find_element(*loc)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.send_keys(text)
        logger.info("输入信息成功")
    def click(self,*loc):
        el=self.find_element(*loc)
        el.click()
        logger.info("这里是成功的点击操作")
    def shuijiao(self,n):
        time.sleep(n)
        logger.info("停一会")
    def switch_dangqian(self):
        # a=self.driver.current_window_handle
        self.driver.switch_to.window(self.a)
        logger.info("这里是当前页面！")
    def switch_to(self,*loc):
        el = self.find_element(*loc)
        self.driver.switch_to.frame(el)
        logger.info("切到frame啦！")
        # dangqian = dir.current_window_handle
        # dir.switch_to.window(dangqian)
    def qieyemian(self,a):
        self.driver.switch_to.window(self.driver.window_handles[a])
        logger.info("切到另一个页面啦！")
    def clear(self,*loc):
        el=self.find_element(*loc)
        el.clear()
        logger.info("这里清除了一个搜索框")
    def hqtext(self,*loc):
        el=self.find_element(*loc)
        logger.info("获取文本值成功。")
        return el.text

    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots'
        rq=time.strftime(" %Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder：/screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.info("Failed to take screenshot! %s"%e)







