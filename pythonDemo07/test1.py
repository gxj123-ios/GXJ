import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Edge()
actions = ActionChains(wd)
wd.implicitly_wait(5)
wd.maximize_window()
wd.get("http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html")
wd.find_element(By.NAME, 'accounts').send_keys('gxja')
wd.find_element(By.NAME, 'pwd').send_keys('123456')
loging_button = wd.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')
actions.click(loging_button).perform()
time.sleep(5)
loging_inp = wd.find_element(By.XPATH, '//*[@id="search-input"]')
loging_inp.send_keys('iphone')
#actions.send_keys(loging_inp, "iphone").perform()
time.sleep(2)
actions.double_click(loging_inp).perform()
time.sleep(5)
wd.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\test_ActionChains01.png')
