from selenium.webdriver.common.by import By
from pythonDemo02.Website.test_report.BasePage import page
import time

class LogingPage(page):
    _url=''
    _username=(By.ID,'username')
    _password=(By.ID,'password')
    _button=(By.CLASS_NAME,'but-flat')

    def username(self,username):
        self.find_element(*self._username).clear()
        self.find_element(*self._username).send_keys(username)

    def password(self,password):
        self.find_element(*self._password).clear()
        self.find_element(*self._password).send_keys(password)

    def button(self,button):
        self.find_element(*button).click()

def login(driver,username,password):
    login_page=LogingPage(driver)
    login_page.open()
    time.sleep(2)
    login_page.username(username)
    login_page.password(password)
    time.sleep(2)
    login_page.button()
