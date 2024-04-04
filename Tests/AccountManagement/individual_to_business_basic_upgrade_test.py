from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.account_management.subscription_upgrade_individual_business_basic import Subscription_upgrade_individual_to_business_basic
from Pages.account_management.password_change import password_change
import time


def test_individual_to_business_basic_upgrade(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential_individual_to_business_basic["validEmail"], loginTestData.valid_credential_individual_to_business_basic["password"])
    skip_account_verification = password_change(driver)
    skip_account_verification.skip_account_verification()
    upgrade_individual_to_business_basic = Subscription_upgrade_individual_to_business_basic(driver)
    upgrade_individual_to_business_basic.upgrade_to_business_basic(driver)
    time.sleep(20)