import unittest
from selenium import webdriver
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
logger=Logger(logger="Base_testcase").getlog()
class Base_testcase(unittest.TestCase):
    def setUp(self):
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        # logger.info("初始化浏览器")

        brow=BrowserEngine()
        self.driver=brow.open_browser()
    def tearDown(self):
        self.driver.quit()
        logger.info("结束")

