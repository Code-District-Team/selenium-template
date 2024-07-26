from config import Config
from Pages.userprofile.onboarding.freelance_onbaording import FreelanceOnboardingPage
from Pages.userprofile.Registration.freerlance_registration_page import FreelanceRegistration
from Pages.businessprofile.businessinfo import Businessinfo


def test_freelance_onboarding(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    Freelance_signup = FreelanceRegistration(driver)
    Freelance_signup.signup_freelance(driver)
    skip_account_verification = Businessinfo(driver)
    skip_account_verification.skip_account_verification()
    freelance_onboarding = FreelanceOnboardingPage(driver)
    freelance_onboarding.freelanceonboarding(driver)


