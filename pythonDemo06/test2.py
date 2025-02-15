import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://127.0.0.1/mgr/sign.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element(By.ID, 'username').send_keys('byhy')
        self.driver.find_element(By.ID, 'password').send_keys('88888888')
        self.driver.find_element(By.CLASS_NAME, 'btn-flat').click()
        time.sleep(2)
    def test_sign(self):
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[0].send_keys('byhy')
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('88888888')
        self.driver.find_element(By.CLASS_NAME, 'btn-flat').click()
        # select=Select(self.driver.find_element(By.NAME, 'btn-flat'))
        # select.select_by_visible_text('测试')


if __name__ == '__main__':
    unittest.main