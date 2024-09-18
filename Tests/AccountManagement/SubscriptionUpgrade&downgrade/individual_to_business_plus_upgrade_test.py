from config import Config
from Pages.login_page import LoginPage
from Pages.userprofile.account_management.upgrade_individual_to_busines_plus import Subscription_upgrade_individual_to_business_plus
from Pages.userprofile.Registration.individualSignupAPI import IndividualSignup
from Pages.businessprofile.businessinfo import Businessinfo
import time


def test_individual_to_business_plus_upgrade(driver_setup):
    loginLog = IndividualSignup()
    email, password = loginLog.test_signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    skipAccountVerification = Businessinfo(driver)
    skipAccountVerification.skip_account_verification()
    skipAccountVerification.skip_account_verification()
    businessPlus = Subscription_upgrade_individual_to_business_plus(driver)
    businessPlus.upgrade_to_business_plus(driver)
