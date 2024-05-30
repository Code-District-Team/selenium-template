import time
from config import Config
from Pages.userprofile.registration.Individual_registration_page import RegistrationPage
from Pages.userprofile.registration.guerilla_mail import GuerrillaMailPage, EmailInboxPage
from Resources.business_registration_data import business_registrationTestData


def take_screenshot(driver, filename):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_path = f"C:/Users/asad.hafeez/PycharmProjects/selenium-template/screenshot/{filename}_{timestamp}.png"
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to {file_path}")


def test_individual_signup(driver_setup):
    driver = driver_setup

    try:
        guerrilla_mail_page = GuerrillaMailPage(driver)
        individual_user = RegistrationPage(driver)
        email_inbox_page = EmailInboxPage(driver)

        # Opening new guerrilla mail to get a new email address
        driver.get("https://www.guerrillamail.com/")
        email_address = guerrilla_mail_page.get_email_address()
        driver.maximize_window()

        # Opening Yoogo application in a new tab
        individual_user.individual_user_signup(email_address)

        email_inbox_page.wait_for_email_list()
        email_inbox_page.click_verification_email()
        otp_digits = email_inbox_page.copy_otp()
        individual_user.authenticating_user(otp_digits)
    except Exception as e:
        print(f"Test failed: {str(e)}")
        take_screenshot(driver, "screenshot")
    finally:
        driver.quit()
