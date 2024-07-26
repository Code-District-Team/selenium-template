import time

from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.userprofile.onboarding import FreelanceOnboardingPage
from Pages.userprofile.Registration.freerlance_registration_page import freelance_registration

def test_freelance_onboarding(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    Freelance_signup = freelance_registration(driver)
    Freelance_signup.signup_freelance(driver)
    freelance_onboarding = FreelanceOnboardingPage(driver_setup)
    freelance_onboarding.freelanceonboarding(driver_setup)
