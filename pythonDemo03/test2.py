import unittest
from csv01 import readCsvv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ddt

@ddt.ddt
class testDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get('http://127.0.0.1/mgr/sign.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()
    data_inpt = readCsvv()
    @ddt.data(*data_inpt)
    def test_1(self,list):
        self.driver.find_element(By.ID, 'username').send_keys('byhy')
        self.driver.find_element(By.ID, 'password').send_keys('88888888')
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT,'药品').click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'btn-md').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(list[0])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys(list[1])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys(list[2])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main