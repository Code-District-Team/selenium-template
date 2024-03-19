from config import Config
from Pages.registration.businessbasic_registration import business_basic_registration




def test_freelance_signup(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    basic_business_user = business_basic_registration(driver)
    basic_business_user.signup_basic_business()
    driver.quit()