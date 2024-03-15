from config import Config
from Pages.registration.Individual_registration_page import RegistrationPage
# from Resources.loginData import loginTestData



def test_individual_signup(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    individual_user = RegistrationPage(driver)
    individual_user.individual_user_signup()


