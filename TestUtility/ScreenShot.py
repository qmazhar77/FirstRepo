from selenium import webdriver

class SS(object):

    def __init__(self,driver):
        self.driver = driver

    def ScreenShot(self,path):
        drictory = "C:/Users/junaid/PycharmProjects/Demo/PytestDemo/ScreenShot"
        self.driver.get_screenshot_as_file(drictory+path)
