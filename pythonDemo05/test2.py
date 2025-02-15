import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get('http://127.0.0.1/mgr/sign.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element(By.CLASS_NAME,'form-control').send_keys('byhy')
        self.driver.find_elements(By.TAG_NAME,'input')[1].send_keys('88888888')
        self.driver.find_element(By.TAG_NAME,'button').click()
        time.sleep(2)
    def test_denglu02(self):
        self.driver.find_element(By.CLASS_NAME, 'form-control').send_keys('byhy')
        self.driver.find_elements(By.TAG_NAME, 'input')[1].send_keys('88888888')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'药品').click()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
if __name__ == '__main__':
    unittest.main()
