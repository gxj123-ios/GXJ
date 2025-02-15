from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

wb = webdriver.Edge()
wb.implicitly_wait(3)
wb.maximize_window()
wb.get('http://127.0.0.1/mgr/sign.html')
wb.find_element(By.ID,'username').send_keys('byhy')
wb.find_element(By.ID,'password').send_keys('88888888')
wb.find_element(By.CLASS_NAME,'btn-flat').click()
#wb.find_elements(By.TAG_NAME,'button')[1].click()
# print(wb.find_elements(By.TAG_NAME,'button')[2].text)
#wb.find_element(By.XPATH,'')
# select=Select(wb.find_element(By.CSS_SELECTOR,''))
# select.select_by_visible_text('测试')
wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_Select01.png')