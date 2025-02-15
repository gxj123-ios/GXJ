import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wb=webdriver.Edge()
wb.get("https://www.saucedemo.com/")
wb.implicitly_wait(5)
wb.find_element(By.NAME,'user-name').send_keys('standard_user')
wb.find_element(By.NAME,'password').send_keys('secret_sauce')
wb.find_element(By.CLASS_NAME,'btn_action').click()
time.sleep(5)
wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_target01.png')