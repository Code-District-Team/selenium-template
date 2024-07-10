import time
<<<<<<< HEAD
=======
from config import Config
from Pages.userprofile.registration.Individual_registration_page import RegistrationPage

from Resources.business_registration_data import business_registrationTestData

>>>>>>> stash

from Pages.userprofile.Registration.Individual_registration_page import RegistrationPage
from Pages.userprofile.Registration.guerilla_mail import GuerrillaMailPage, EmailInboxPage
def take_screenshot(driver, filename):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_path = f"C:/Users/asad.hafeez/PycharmProjects/selenium-template/screenshot/{filename}_{timestamp}.png"
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to {file_path}")


def test_individual_signup(driver_setup):
    driver = driver_setup

    try:

        driver.get(Config.base_url)
        driver.maximize_window()
        individual_signup = RegistrationPage(driver)
        individual_signup.individual_user_signup()
        take_screenshot(driver, "screenshot")

    except Exception as e:
        print(f"Test failed: {str(e)}")
        take_screenshot(driver, "screenshot")

