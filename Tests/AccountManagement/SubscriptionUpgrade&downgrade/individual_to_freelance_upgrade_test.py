from config import Config
from Pages.login_page import LoginPage
from Pages.userprofile.account_management.subscription_upgrade_individual_to_freelance import Subscription_upgrade_individual_to_freelance
import time
from Pages.userprofile.Registration.individualSignupAPI import IndividualSignup
from Pages.businessprofile.businessinfo import Businessinfo

def test_individual_to_freelance_upgrade(driver_setup):
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
    freelanceSubscriptionUpgrade = Subscription_upgrade_individual_to_freelance(driver)
    freelanceSubscriptionUpgrade.upgrade_subcription_indvidual_to_free_lance(driver)

