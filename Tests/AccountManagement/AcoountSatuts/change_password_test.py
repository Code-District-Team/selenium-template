import time

from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.userprofile.account_management.password_change import password_change


def test_change_password(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential_busniess_basic_to_business_plus["validEmail"], loginTestData.valid_credential_busniess_basic_to_business_plus["password"])
    time.sleep(20)
    change_password = password_change(driver)
    change_password.change_password(driver)



