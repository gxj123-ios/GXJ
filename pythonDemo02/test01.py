import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class PytestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://127.0.0.1/mgr/sign.html")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test_denglun01(self):
        self.driver.find_element(By.ID,'username').send_keys('byhy')
        self.driver.find_element(By.ID,'password').send_keys('88888888')
        self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[3]/div/button').click()
        time.sleep(2)
    def test_denglun02(self):
        self.driver.find_element(By.ID, 'username').send_keys('byhy')
        self.driver.find_element(By.ID, 'password').send_keys('88888888')
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, '客户').click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_target02.png')


if __name__ == '__main__':
    unittest.main()