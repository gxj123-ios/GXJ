import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wb= webdriver.Chrome()
wb.maximize_window()
wb.implicitly_wait(5)
wb.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')
wb.find_element(By.NAME, 'accounts').send_keys('gxja')
wb.find_element(By.NAME, 'pwd').send_keys('123456')
wb.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()
# wb.find_element(By.LINK_TEXT,'供应商信息').click()
# wb.find_elements(By.LINK_TEXT,'查看')[0].click()
# var = wb.window_handles[1]
time.sleep(2)
# wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_handles.png')