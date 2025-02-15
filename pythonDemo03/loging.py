import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wb = webdriver.Edge()
wb.get("http://127.0.0.1/mgr/sign.html")
wb.implicitly_wait(5)
wb.maximize_window()
# wb.find_element(By.ID, "username").send_keys("byhy")
# wb.find_element(By.ID, "password").send_keys("88888888")
# wb.find_element(By.TAG_NAME, "button").click()
# wb.find_element(By.PARTIAL_LINK_TEXT, "药品").click()
# wb.find_element(By.TAG_NAME, 'label').click()
# print(wb.find_element(By.TAG_NAME, 'label').text)
# time.sleep(2)

wb.find_element(By.ID, 'username').send_keys('byhy')
wb.find_element(By.ID, 'password').send_keys('88888888')
wb.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()
time.sleep(2)
wb.find_element(By.LINK_TEXT, '客户').click()
time.sleep(2)
wb.find_element(By.CLASS_NAME, 'btn-md').click()
time.sleep(2)
wb.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()
time.sleep(2)
wb.switch_to.alert.accept()
time.sleep(2)
# 弹窗  alert = wb.switch_to.alert
# 同意  alert.accept()
# 取消  alert.dismiss()
