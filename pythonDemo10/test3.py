import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from csvv import readCsv

@ddt.ddt
class test3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://127.0.0.1/mgr/sign.html')

    def tearDown(self):
        self.driver.quit()

    data_inp = readCsv()
    @ddt.data(*data_inp)
    def test1(self,list):
        self.driver.find_element(By.ID, 'username').send_keys('byhy')
        self.driver.find_element(By.ID, 'password').send_keys('88888888')
        self.driver.find_element(By.CLASS_NAME, 'btn-flat').click()
        self.driver.find_element(By.LINK_TEXT, '药品').click()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/button').click()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(list[0])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys(list[1])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys(list[2])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()

        # try:
        #     self.assertEquals('','')
        #
        # except:
        #     self.driver.get_screenshot_as_file(r'')


if __name__ == '__main__':
    unittest.main()

