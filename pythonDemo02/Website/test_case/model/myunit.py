import unittest

from pythonDemo02.driver.driver import getWebDriver

class TestDemo(unittest.TestCase):
    def setUp(self)->None:
        self.driver =getWebDriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def tearDown(self)->None:
        self.driver.quit()