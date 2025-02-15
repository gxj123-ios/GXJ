import unittest
import time
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from csvv import readCsv
@ddt.ddt
class TestDemoPlus(unittest.TestCase):
    def setUp(self)->None:
        self.driver = webdriver.Edge()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self)->None:
        self.driver.quit()
    data_inpt = readCsv()
    @ddt.data(*data_inpt)
    def testDemo01(self,list):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="first-name"]').send_keys(list[0])
        self.driver.find_element(By.XPATH,'//*[@id="last-name"]').send_keys(list[1])
        self.driver.find_element(By.XPATH,'//*[@id="postal-code"]').send_keys(list[2])
        time.sleep(2)
        self.driver.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\ccc.png')
        self.driver.find_element(By.XPATH,'//*[@id="continue"]').click()

if __name__ == '__main__':
    unittest.main