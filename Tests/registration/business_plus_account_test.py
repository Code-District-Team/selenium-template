import time

from Pages.userprofile.Registration.business_plus_registration import BusinessPlus

from config import Config



def test_business_plus_signup(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    businessPlus_signup = BusinessPlus(driver)
    businessPlus_signup.business_plus_signup(driver)
    time.sleep(15)

