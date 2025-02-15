import os
import csv
def  screenshot(driver,filename):
    path = os.path.dirname(__file__)
    path = str(path).replace("\\",'/')
    filename = path +"/Website/test_report/srceenshot"+ filename
    driver.get_screenshot_as_file(filename)

def readTestDemo(line):
    with open("F:\testData.csv",'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader,1):
            if index==line:
                return row