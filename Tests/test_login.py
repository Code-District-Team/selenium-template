
from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData




def test_login_valid_credentials(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
