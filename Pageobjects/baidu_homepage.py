from Pageobjects.base import BasePage
from selenium.webdriver.common.by import By
class HomePage(BasePage):
    home_page_input=(By.ID,'kw')
    home_page_button=(By.ID,'su')

    def shuru(self,text):
        self.sendkeys(text,*self.home_page_input)
        self.click(*self.home_page_button)

