import os
from _datetime import datetime
from datetime import date
from selenium import webdriver
class TimeStamp(object):

    #def __init__(self,driver):
     #   self.driver = driver

     def folder(self,Path):

        project = "ScreenShot"
        Module = "Test_MercuryTours_SignOn"

        today = datetime.datetime.now()
        now_string = str(today.strftime(("%Y-%m-%d_%A_%H_%M_%S")))

        print (now_string)
        #root ="D:/"
        root="."
        path = f"{root}/{project}/{Module}/{now_string}/"

        print(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            os.removedirs(path)

