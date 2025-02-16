import time
import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from csvv import readCsv

@ddt.ddt

class test3(unittest.TestCase):
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
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,'个人中心').click()
        self.driver.find_element(By.LINK_TEXT,'我的地址').click()
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div[1]/button').click()
        # 通过window_handles方法将标签页切换到第二个标签
        # self.driver.execute_script("window.open(“http://shop-xo.hctestedu.com/index.php?s=/index/useraddress/saveinfo.html“, “_blank“);")
        # handles = self.driver.window_handles
        # if len(handles) >= 2:
        #     self.driver.switch_to.window(handles[1])
        #     print("已切换到第二个标签页，当前页面标题：", self.driver.title)
        # self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div[1]/span').click()
        # self.driver.find_element(By.XPATH, '/html/body/div[1]/form/div[2]/input').send_keys(list[1])
        # self.driver.find_element(By.NAME, 'tel').send_keys(list[2])
        # self.driver.find_element(By.NAME, 'address').send_keys(list[3])
        # self.driver.find_element(By.XPATH, '/html/body/div[1]/form/div[7]/button').click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
