from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to_frame(0)
#driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("D://Azhar Python/PythonFramework/ScreenShot.png")
