import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo(unittest.TestCase):
    def setUp(self)->None:
        self.wb=webdriver.Edge()
        self.wb.get("http://127.0.0.1/mgr/sign.html")
        self.wb.maximize_window()
        self.wb.implicitly_wait(3)
    def tearDown(self)->None:
        self.wb.quit()

    def test_denglu01(self):
        self.wb.find_element(By.ID,'username').send_keys('byhy')
        self.wb.find_element(By.ID,'password').send_keys('88888888')
        self.wb.find_element(By.CLASS_NAME,'btn-flat').click()
        time.sleep(2)
    def test_denglu02(self):
        self.wb.find_element(By.ID, 'username').send_keys('byhy')
        self.wb.find_element(By.ID, 'password').send_keys('88888888')
        self.wb.find_element(By.TAG_NAME, 'button').click()
        self.wb.find_element(By.LINK_TEXT, '药品').click()
        self.wb.find_element(By.LINK_TEXT,'尾页').click()
        time.sleep(2)
        self.wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\denglu02.png')

    def test_denglu03(self):
        self.wb.find_element(By.ID, 'username').send_keys('byhy')
        self.wb.find_element(By.ID, 'password').send_keys('88888888')
        self.wb.find_element(By.TAG_NAME, 'button').click()
        self.wb.find_element(By.LINK_TEXT, '药品').click()
        # 六
        # 1. 找到第一条数据的“查看”链接
        link = self.wb.find_element(By.XPATH, '//*[@id="root"]/footer/a')
        # 2. 删除 target 属性
        self.wb.execute_script("arguments[0].removeAttribute('target');", link)
        link.click()
        time.sleep(2)
        self.wb.get_screenshot_as_file(r'C:\Users\Lenovo\Pictures\联想截图\denglu03.png')
if __name__ == '__main__':
    unittest.main()