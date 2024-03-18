from config import Config
from Pages.registration.freerlance_registration_page import freelance_registration
# from Resources.loginData import loginTestData



def test_freelance_signup(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    freelance_user = freelance_registration(driver)
    freelance_user.signup_freelance_user()
    driver.quit()


