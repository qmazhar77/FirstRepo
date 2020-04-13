import pytest
from selenium import webdriver
import allure

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()
@allure.description("Validates OrangeHRM with valid login crendentials")
@allure.severity(severity_level="CRITICAL")
def test_validLogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").clear()
    enter_username("admin")
    driver.find_element_by_id("txtPassword").clear()
    enter_password("admin123")
    driver.find_element_by_id("btnLogin").click()
    assert "dashboard" in driver.current_url

@allure.description("Validates OrangeHRM with Invalid login crendentials")
@allure.severity(severity_level="NORMAL")

def test_InvalidLogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").clear()
    enter_username("admin")
    driver.find_element_by_id("txtPassword").clear()
    enter_password("admin123")

    driver.find_element_by_id("btnLogin").click()
    try:
        assert "dashboard" in driver.current_url
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),name="Invalid Credential",attachment_type=allure.attachment_type.PNG)

@allure.step("Entering user name as (0)")
def enter_username(username):
    driver.find_element_by_id("txtUsername").send_keys(username)
@allure.step("Entering password as (0)")
def enter_password(password):
    driver.find_element_by_id("txtPassword").send_keys(password)

# we can execute this command from command prompt as well as terminal
#C:\Users\junaid\PycharmProjects\Demo> pytest -v -s pytestdemo\test_login.py --alluredir=jreports
