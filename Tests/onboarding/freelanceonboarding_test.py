import time

from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.userprofile.onboarding import FreelanceOnboardingPage

def test_freelance_onboarding(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential_individual_to_freelance["validEmail"], loginTestData.valid_credential_individual_to_freelance["password"])
    time.sleep(20)
    freelance_onboarding = FreelanceOnboardingPage(driver_setup)
    freelance_onboarding.freelanceonboarding(driver_setup)