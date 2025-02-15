import unittest
import time
import ddt
from csvv1 import readCsvv
from selenium import webdriver
from selenium.webdriver.common.by import By

@ddt.ddt
class testDemo(unittest.TestCase):
    def setUp(self)->None:
        self.driver = webdriver.Edge()
        self.driver.get("http://127.0.0.1/mgr/sign.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self)->None:
        self.driver.quit()

    data_inpt = readCsvv()
    @ddt.data(*data_inpt)
    def test01(self,list):
        self.driver.find_element(By.ID, 'username').send_keys('byhy')
        self.driver.find_element(By.ID, 'password').send_keys('88888888')
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'btn-md').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(list[0])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys(list[1])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys(list[2])
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()
        self.driver.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_target03.png')
if __name__ == '__main__':
    unittest.main()
