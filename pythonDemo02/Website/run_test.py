import time
import unittest

import HtmlTestRunner
from HtmlTestRunner import *
test_dir="./Website/test_report"
report_dir="./Website/test_case"
discover=unittest.defaultTestLoader.discover(test_dir,'test_add.py')
now=time.strftime("%Y-%m-%d %H:%M:%S")
report_name=report_dir+"/"+now+"result.html"
with open(report_name,'wb') as f:
    runner = HtmlTestRunner(stream=f,title="TestReport",descriptions="erp test")
    runner.run(discover)