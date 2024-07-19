from config import Config
from Pages.login_page import LoginPage
from Pages.userprofile.account_management.subscription_upgrade_individual_business_basic import Subscription_upgrade_individual_to_business_basic
import time
from Pages.userprofile.registration.test_individualSignupAPI import IndividualSignup
from Pages.businessprofile.businessinfo import Businessinfo



def test_individual_to_business_basic_upgrade(driver_setup):
    loginLog = IndividualSignup()
    email, password = loginLog.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    skipAccountVerification = Businessinfo(driver)
    skipAccountVerification.skip_account_verification()
    upgrade_individual_to_business_basic = Subscription_upgrade_individual_to_business_basic(driver)
    upgrade_individual_to_business_basic.upgrade_to_business_basic(driver)
    time.sleep(20)