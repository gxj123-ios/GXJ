import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class test2(unittest.TestCase):
    def setUp(self)->None:
        self.driver = webdriver.Edge()
        self.driver.get("http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def tearDown(self)->None:
        self.driver.quit()

    def test_login(self):
        self.driver.find_element(By.NAME,'accounts').send_keys('gxja')
        # pwd=self.driver.find_elements(By.CLASS_NAME, 'am-field-error')
        # pwd[1].send_keys('123456')
        self.driver.find_element(By.NAME, 'pwd').send_keys('123456')
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()
        time.sleep(2)
    def test_login2(self):
        self.driver.find_element(By.NAME,'accounts').send_keys('gxja')
        self.driver.find_element(By.NAME, 'pwd').send_keys('123456')
        # self.driver.find_element(By.CLASS_NAME, 'am-active').send_keys('123456')
        # self.driver.find_element(By.TAG_NAME, 'button').click()
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()

        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,'个人中心').click()
        # self.driver.find_elements(By.TAG_NAME, 'button')[0].click()
        # self.driver.switch_to.alert.dismiss()
if __name__ == '__main__':
    unittest.main()