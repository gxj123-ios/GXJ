from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("secret_sauce")
driver.find_element(By.XPATH,'//*[@id="login-button"]').click()
sleep(5)
driver.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\aaa.png')