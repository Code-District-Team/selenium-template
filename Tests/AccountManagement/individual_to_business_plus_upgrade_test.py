from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.account_management.password_change import password_change
from Pages.account_management.upgrade_individual_to_busines_plus import Subscription_upgrade_individual_to_business_plus
import time


def test_individual_to_business_plus_upgrade(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential_individual_to_business_plus["validEmail"], loginTestData.valid_credential_individual_to_business_plus["password"])
    time.sleep(30)
    skip_account_verification = password_change(driver)
    skip_account_verification.skip_account_verification()
    upgrade_individual_to_business_plus = Subscription_upgrade_individual_to_business_plus(driver)
    upgrade_individual_to_business_plus.upgrade_to_business_plus(driver)
    subscription_payment = Subscription_upgrade_individual_to_business_plus(driver)
    subscription_payment.payment_for_subscription_upgrade(driver)
    time.sleep(20)