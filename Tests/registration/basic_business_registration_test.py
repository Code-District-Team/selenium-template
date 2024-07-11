
from Pages.userprofile.registration.businessbasic_registration import BusinessBasicRegistration
from config import Config



def test_business_basic(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    individual_signup = BusinessBasicRegistration(driver)
    individual_signup.signup_basic_business(driver)