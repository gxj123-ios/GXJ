import time
import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from csvv import readCsv

@ddt.ddt
class testDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')

    def tearDown(self):
        self.driver.quit()
    data_inp = readCsv()
    @ddt.data(*data_inp)
    def test_login(self,list):
        self.driver.find_element(By.NAME, 'accounts').send_keys('gxja')
        self.driver.find_element(By.NAME, 'pwd').send_keys('123456')
        # self.driver.find_element(By.TAG_NAME, 'button').click()
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()

        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, '个人中心').click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, '我的地址').click()
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div[1]/button').click()
        # self.driver.find_element(By.XPATH,'/html/body/div[1]/form/div[1]/input').send_keys(list[0])
        self.driver.get('http://shop-xo.hctestedu.com/index.php?s=/index/useraddress/saveinfo.html')
        self.driver.find_element(By.NAME,'name').send_keys(list[1])
        self.driver.find_element(By.NAME,'tel').send_keys(list[2])
        self.driver.find_element(By.NAME,'address').send_keys(list[3])
        self.driver.find_element(By.XPATH,'/html/body/div[1]/form/div[7]/button').click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
