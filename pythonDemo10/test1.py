import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wb = webdriver.Chrome()
wb.maximize_window()
wb.get('http://127.0.0.1/mgr/sign.html')
wb.implicitly_wait(3)
wb.find_element(By.ID, 'username').send_keys('byhy')
wb.find_element(By.ID, 'password').send_keys('88888888')
wb.find_element(By.TAG_NAME, 'button').click()
wb.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
wb.switch_to.alert.dismiss()
time.sleep(1)
# wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_accept01.png')
