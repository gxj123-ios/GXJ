from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
wb = webdriver.Edge()
wb.get('http://127.0.0.1/mgr/sign.html')
wb.implicitly_wait(5)
wb.maximize_window()
wb.find_element(By.ID,'username').send_keys('byhy')
wb.find_element(By.ID,'password').send_keys('88888888')
wb.find_element(By.CLASS_NAME,'btn-flat').click()
wb.find_element(By.PARTIAL_LINK_TEXT, "药品").click()
time.sleep(2)
b = (wb.find_elements(By.TAG_NAME, 'label')[0])
print(b.text)
b.click()
a = (wb.find_elements(By.TAG_NAME, 'label')[0])
print(a.text)
a.click()

#wb.find_element(By.NAME,'username').send_keys('aaa.png')
wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\denglu.png')