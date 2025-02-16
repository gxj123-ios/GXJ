import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wb = webdriver.Chrome()
wb.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')
wb.maximize_window()
wb.implicitly_wait(3)
time.sleep(3)
wb.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input').send_keys('gjxa')
wb.find_elements(By.TAG_NAME, 'input')[3].send_keys('123456')
# a = wb.find_element(By.CLASS_NAME,'btn-loading-example')
# print(a)
# a.click()
b=wb.find_elements(By.TAG_NAME,'button')[4]
print(b)
b.click()
# 滚动条下拉
wb.execute_script('window.scrollTo(0, 500)')
time.sleep(10)
# a = wb.find_element(By.CLASS_NAME,'am-collapsed')
# print(a)
# b = wb.find_elements(By.TAG_NAME,'li')
# print(b)
# select = Select(wb.find_elements(By.XPATH,''))
# select.by_value_text('测试')

# wb.get_screenshot_as_file(r'')