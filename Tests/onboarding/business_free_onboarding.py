import time

from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.onboarding.onboarding_page import OnboardingPage

def test_business_free_onboarding(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
    time.sleep(10)
    business_free_onboarding = OnboardingPage(driver)

    business_free_onboarding.onboarding_start()