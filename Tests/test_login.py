from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData



def test_login_with_empty_fields(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    login_page.login_with_empty_fields()


def test_login_valid_credentials(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
