import unittest
from selenium import webdriver
from time import sleep
from datetime import datetime
from PytestDemo.Pages.loginPage1 import LoginPage

class test_ScreenShot:
    def ss(self):
        self.driver = self.driver
        filepath = "C:/Users/junaid/PycharmProjects/Demo/PytestDemo/ScreenShot/Test_MercuryTours_SignOn/"
        currentTime = datetime.now()
        pictime = currentTime.strftime("%Y_%m_%d-%H_%M_%S")
        picName = pictime + '.png'
        completefilepath = filepath + picName
        self.driver.save_screenshot(completefilepath)


class test_MercuryTours_SignOn(test_ScreenShot):

    def test_SignOnPage(self):

        driver = self.driver

        self.driver.get("http://newtours.demoaut.com/")
        self.driver.implicitly_wait(10)

# creating object of ss screenshot utility
        if driver.title == "Welcome: Mercury Tours":
            print ("Sign On Page Loaded Successfully")
            #driver.save_screenshot("C:/Users/junaid/PycharmProjects/Demo/PytestDemo/ScreenShot/SingOn.png")
            #CurTime = datetime.now()
            #picName = CurTime.strftime("%Y_%m_%d_%H_%M_%S")
            obj = test_ScreenShot()
            obj.ss("SignOn.png")


        else:
            print("Sign On Page Load To Fail")
        login = LoginPage(driver)
        try:
            print("Provide Invalid User Name")
            #driver.find_element_by_name("userName").send_keys("Invalid")
            login.username_text_name.send_keys("mer")
            print("Provide Invalid Password")
            #driver.find_element_by_name("password").send_keys("Invalid")
            login.password_text_name.send_keys("mer")
            #driver.save_screenshot("C:/Users/junaid/PycharmProjects/Demo/PytestDemo/ScreenShot/InvalidID.png")
            obj.ss("_InvalidId.png")
            sleep(3)
            #driver.find_element_by_name("login").click()
            print("Click on Login Button")
            login.login_button_name.click()
            sleep(3)
            if driver.title == "Sign-on: Mercury Tours":
                print ("Invalid credential Provided")
                obj.ss("_LoginDeny.png")
                #driver.save_screenshot("C:/Users/junaid/PycharmProjects/Demo/PytestDemo/ScreenShot/LoginDeny.png")
        except Exception as e:
                print ("Exception Occurred" + e)

if __name__ == "__main__":
    unittest.main()

