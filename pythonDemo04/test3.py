import unittest

import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from csvv import readCsv
@ddt.ddt
class testDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get('http://127.0.0.1/mgr/sign.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
    data_inp = readCsv()
    @ddt.data(*data_inp)
    def test1(self,list):
        self.driver.find_element(By.CLASS_NAME,'form-control').send_keys('byhy')
        self.driver.find_element(By.ID,'password').send_keys('88888888')
        self.driver.find_element(By.TAG_NAME,'button').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'药品').click()
        self.driver.find_elements(By.TAG_NAME,'button')[0].click()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(list[0])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys(list[1])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys(list[2])
        self.driver.find_element(By.CLASS_NAME,'btn-xs').click()


if __name__ == '__main__':
    unittest.main()
