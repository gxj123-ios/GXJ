import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('http://127.0.0.1/mgr/sign.html')

    def tearDown(self):
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.ID,'username').send_keys('byhy')
        self.driver.find_element(By.ID,'password').send_keys('88888888')
        self.driver.find_element(By.CLASS_NAME,'btn-flat').click()
        time.sleep(1)


    def test_denglu02(self):
        self.driver.find_element(By.ID, 'username').send_keys('byhy')
        self.driver.find_element(By.ID, 'password').send_keys('88888888')
        self.driver.find_element(By.CLASS_NAME, 'btn-flat').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT,'药品').click()

if __name__ == '__main__':
    unittest.main()
