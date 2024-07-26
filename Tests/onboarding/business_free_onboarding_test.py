import time

from selenium.webdriver.support.wait import WebDriverWait

from Pages.businessprofile.businessinfo import Businessinfo
from Pages.userprofile.Registration.businessbasicSignupAPI import BusinessBasicSignup
from Pages.userprofile.onboarding.onboarding_page import OnboardingPage
from Utils.onboardingLocators import onboardingLocators
from config import Config
from Pages.login_page import LoginPage

from selenium.webdriver.support import expected_conditions as EC
from Utils.profile_locators import profileLocators


def test_business_free_onboarding(driver_setup):
    loginLog = BusinessBasicSignup()
    email, password = loginLog.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    skipAccountVerification = Businessinfo(driver)
    skipAccountVerification.skip_account_verification()

    business_free_onboarding = OnboardingPage(driver)
    business_free_onboarding.onboarding_start()




