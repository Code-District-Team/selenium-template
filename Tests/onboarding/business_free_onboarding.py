from config import Config
from Pages.onboarding.onboarding_page import OnboardingPage

def test_business_free_onboarding(driver_setup):
    driver = driver_setup

    business_free_onboarding = OnboardingPage(driver)