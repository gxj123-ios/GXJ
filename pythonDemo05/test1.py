

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

wb=webdriver.Edge()
wb.get("http://127.0.0.1/mgr/sign.html")
wb.implicitly_wait(3)
wb.maximize_window()
wb.find_element(By.ID,'username').send_keys('byhy')
wb.find_element(By.ID,'password').send_keys('88888888')
wb.find_element(By.TAG_NAME,'button').click()
# select1 = Select(wb.find_element(By.CSS_SELECTOR,'button').click())
# select1.select_by_index('测试')
# select2 = Select(wb.find_element(By.XPATH,'button').click())
# select2.select_by_value('测试')
wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_Select01.png')
