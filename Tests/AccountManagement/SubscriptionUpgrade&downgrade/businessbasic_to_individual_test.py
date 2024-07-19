from config import Config
from Pages.login_page import LoginPage
from Pages.userprofile.account_management.susbscription_downgrade_businessbasic_to_individual import Subscription_downgrade_business_basic_to_individual
from Pages.userprofile.registration.test_businessbasicSignupAPI import BusinessBasicSignup
from Pages.businessprofile.businessinfo import Businessinfo


def test_business_basic_to_individual_downgrade(driver_setup):
    loginLog = BusinessBasicSignup()
    email, password = loginLog.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    skipAccountVerification = Businessinfo(driver)
    skipAccountVerification.skip_account_verification()
    downgrade_to_individual = Subscription_downgrade_business_basic_to_individual(driver)
    downgrade_to_individual.subscription_downgrade_business_basic_to_individual(driver)