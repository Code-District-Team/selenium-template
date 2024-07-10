import time


from Pages.login_page import LoginPage
from Pages.userprofile.account_management.account_status import AccountStatus
from Resources.loginData import loginTestData
from config import Config


def test_account_suspend_activation(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential_individual_to_business_basic["validEmail"], loginTestData.valid_credential_individual_to_business_basic["password"])
    time.sleep(20)
    account_suspend = AccountStatus(driver)
    account_suspend.test_account_suspend_and_activation()


