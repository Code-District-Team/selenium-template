import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData

@pytest.fixture(scope="module")
def setup(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_login_invalid_credentials(setup):
    driver = setup
    driver.get("https://staging.source2.link/login")
    login_page = LoginPage(driver)
    login_page.login(loginTestData.invalid_credentials["InvalidEmail"], loginTestData.invalid_credentials["invalidPassword"])
    login_page.email_error_message()



def test_login_valid_credentials(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
