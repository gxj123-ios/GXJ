import os
import csv
def screenshot(dirver,filename):
    path=os.path.dirname(__file__)
    path=str(path).replace("\\","/")
    filename=path+"/"+filename