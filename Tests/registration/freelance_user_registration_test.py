import time

from config import Config
from Pages.userprofile.Registration.freerlance_registration_page import FreelanceRegistration




def test_freelance_signup(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    Freelance_signup = FreelanceRegistration(driver)
    Freelance_signup.signup_freelance(driver)


