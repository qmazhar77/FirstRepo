import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from selenium import webdriver
from PytestDemo.Utilles.XlUtilles import XlUtilles
from selenium.webdriver import ActionChains
import unittest
import HtmlTestRunner

class OrangLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()


    def test_login1_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        path =("D://Azhar Python/Login.xlsx")
        rows = XlUtilles.getRowsCount(path,'Sheet1')

        for r in range(2,rows+1):
            UserName = XlUtilles.readData(path,"Sheet1",r,1)
            PassWord = XlUtilles.readData(path,"Sheet1",r,2)

            driver.find_element_by_id("txtUsername").clear()
            driver.find_element_by_id("txtUsername").send_keys(UserName)
            driver.find_element_by_id("txtPassword").clear()
            driver.find_element_by_id("txtPassword").send_keys(PassWord)

            driver.find_element_by_id("btnLogin").click()

        if driver.title=="OrangeHRM":
            print("Test case pass")
            XlUtilles.writeData(path,"Sheet1",r,3,"Test Pass")
        else:
            print("Test case Fail")
            XlUtilles.writeData(path,"Sheet1",r,3,"Test Failed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.find_element_by_id("welcome").click()
        Logout =  cls.driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a")
        actions = ActionChains(cls.driver)
        actions.move_to_element(Logout).click().perform()
        cls.driver.close()

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/junaid/PycharmProjects/Demo/PytestDemo/OrangeHTMLReports'))

#python -m scr.Login.py
