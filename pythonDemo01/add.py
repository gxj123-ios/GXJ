import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class TestDemo(unittest.TestCase):
    def setUp(self)->None:
        self.driver = webdriver.Edge()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def tearDown(self)->None:
        self.driver.quit()
    def testDemo1(self):
        self.driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("standard_user")
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("secret_sauce")
        self.driver.find_element(By.XPATH,'//*[@id="login-button"]').click()
        sleep(2)
        self.driver.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\aaa.png')
    def testDemo2(self):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
        sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="checkout"]').click()
        sleep(2)
        self.driver.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\bbb.png')


if __name__ == '__main__':
    unittest.main