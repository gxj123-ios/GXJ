from selenium.webdriver.common.by import By
from pythonDemo02.Website.test_report.BasePage import page
import time

class AddPage(page):
    url=''
    _title=(By.LINK_TEXT,'客户')
    _add=(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/button')
    _name=(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input')
    _phone=(By.CLASS_NAME,'from-control')
    _site=(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea')
    _testbut=(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/button')

    def title(self):
        self.find_element(*self._title).click()

    def add(self):
        self.find_element(*self._add).click()

    def name(self):
        self.find_element(*self._name).clear()
        self.find_element(*self._name).send_keys(self.name)

    def phone(self):
        self.find_element(*self._phone).clear()
        self.find_element(*self._phone).send_keys(self.phone)

    def site(self):
        self.find_element(*self._site).clear()
        self.find_element(*self._site).send_keys(self.site)

    def testbut(self):
        self.find_element(*self._testbut).click()

def addPage(drivere,name,phone,site):
    add_page=AddPage(drivere)
    add_page.title()
    add_page.add()
    add_page.name(name)
    add_page.phone(phone)
    add_page.site(site)
    time.sleep(2)
    add_page.testbut()