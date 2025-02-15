import time

from pythonDemo02.Website.test_report.LogingPage import *
from pythonDemo02.Website.test_report.AddPage import *
from pythonDemo02.Website.test_case.model import function,myunit
import ddt

@ddt.ddt
class TestAdd(myunit.TestDemo):
    @ddt.data(*function.readTestDemo(*range(1,7)))
    def test_(self,value):
        testdata_01=function.readTestDemo({value})
        login(self.wb,'byhy','88888888')
        addPage(self.wb, testdata_01[0])
        text_01=AddPage(self.wb).textPass()
        time.sleep(2)
        function.screenshot(self.wb,"test_01.png")
        self.assertTrue(text_01,testdata_01)