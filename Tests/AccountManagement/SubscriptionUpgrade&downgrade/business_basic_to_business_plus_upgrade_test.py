from config import Config
from Pages.login_page import LoginPage
from Pages.userprofile.Registration.businessbasicSignupAPI import BusinessBasicSignup
from Pages.businessprofile.businessinfo import Businessinfo
from Pages.userprofile.account_management.subscription_upgrade_business_basic_to_business_plus import Subscription_upgrade_business_basic_to_business_plus

import time


def test_individual_to_business_plus_upgrade(driver_setup):
    loginLog = BusinessBasicSignup()
    email, password = loginLog.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    time.sleep(10)
    skipAccountVerification = Businessinfo(driver)
    skipAccountVerification.skip_account_verification()
    skipAccountVerification.skip_account_verification()
    upgrade_individual_to_business_plus = Subscription_upgrade_business_basic_to_business_plus(driver)
    upgrade_individual_to_business_plus.upgrade_to_business_plus(driver)
    time.sleep(5)