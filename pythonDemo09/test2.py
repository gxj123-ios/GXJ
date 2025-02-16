import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element(By.NAME, 'accounts').send_keys('gxja')
        self.driver.find_element(By.NAME, 'pwd').send_keys('123456')
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()
    def test_logout(self):
        self.driver.find_element(By.NAME, 'accounts').send_keys('gxja')
        self.driver.find_elements(By.TAG_NAME, 'input')[3].send_keys('123456')
        self.driver.find_elements(By.TAG_NAME,'button')[4].click()
        # self.driver.find_element(By.LINK_TEXT,'供应商信息').click()
        # self.driver.find_element(By.XPATH,'').click()
        # self.driver.switch_to.window(driver.window_handles[1])

if __name__ == '__main__':
    unittest.main()
