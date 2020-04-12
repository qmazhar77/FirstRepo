from selenium import webdriver
from scr.xlUtills import XlUtilles
from selenium.webdriver import ActionChains
import unittest
import HTMLTestRunner

class OrangLogin(unittest.TestCase):


    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    path =("D://Azhar Python/Login.xlsx")
    rows = XlUtilles.getRowsCount(path,'Sheet1')

    for r in range(2,rows+1):
        username = XlUtilles.readData(path,"Sheet1",r,1)
        password = XlUtilles.readData(path,"Sheet1",r,2)

        driver.find_element_by_id("txtUsername").send_keys(username)
        #driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys(username)
        driver.find_element_by_id("txtPassword").send_keys((password))
        driver.find_element_by_id("btnLogin").click()

        if driver.title=="OrangeHRM":
            print("Test case pass")
            XlUtilles.writeData(path,"Sheet1",r,3,"Test Pass")
        else:
            print("Test case Fail")
            XlUtilles.writeData(path,"Sheet1",r,3,"Test Failed")

        driver.find_element_by_id("welcome").click()
        Logout =  driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a")
        actions = ActionChains(driver)
        actions.move_to_element(Logout).click().perform()
        driver.close()

if __name__ == '__main__':
     unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='C:/Users/junaid/PycharmProjects/OrangeHRMAutomation/Reports'))

#python -m scr.Login.py
