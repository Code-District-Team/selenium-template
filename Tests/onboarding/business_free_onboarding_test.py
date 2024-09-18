from Pages.businessprofile.businessinfo import Businessinfo
from Pages.userprofile.Registration.businessbasic_registration import BusinessBasicRegistration
from Pages.userprofile.onboarding.onboarding_page import OnboardingPage
from config import Config



def test_business_free_onboarding(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    businessbasic_signup = BusinessBasicRegistration(driver)
    businessbasic_signup.signup_basic_business(driver)
    skipAccountVerification = Businessinfo(driver)
    skipAccountVerification.skip_account_verification()
    skipAccountVerification.skip_account_verification()

    business_free_onboarding = OnboardingPage(driver)
    business_free_onboarding.onboarding_start()
