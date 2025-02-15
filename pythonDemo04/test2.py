import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class testDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://127.0.0.1/mgr/sign.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        input1 = self.driver.find_elements(By.TAG_NAME, "input")
        if input1:
            input1[0].send_keys('byhy')
            input1[1].send_keys('88888888')
        else:
            print('没有找到输入框')
        self.driver.find_element(By.CLASS_NAME,'btn-flat').click()
        time.sleep(2)

    def test_login_2(self):
        self.driver.find_element(By.CLASS_NAME,'form-control').send_keys('byhy')
        self.driver.find_element(By.ID,'password').send_keys('88888888')
        self.driver.find_element(By.TAG_NAME,'button').click()
        # select = Select(self.driver.find_element(By.CLASS_NAME,'pull-right'))
        # select.select_by_value('测试')
        time.sleep(2)

if __name__ == '__main__':
    unittest.main