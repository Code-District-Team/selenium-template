from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.userprofile.account_management.upgrade_individual_to_busines_plus import Subscription_upgrade_individual_to_business_plus
from Pages.registration.payment_page import payment_processing
import time


def test_individual_to_business_plus_upgrade(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential_individual_to_business_plus["validEmail"], loginTestData.valid_credential_individual_to_business_plus["password"])
    time.sleep(10)
    upgrade_individual_to_business_plus = Subscription_upgrade_individual_to_business_plus(driver)
    upgrade_individual_to_business_plus.upgrade_to_business_plus(driver)
    subscription_payment = payment_processing(driver)
    subscription_payment.payment_processing()
    time.sleep(20)