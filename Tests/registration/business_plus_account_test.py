import time

from Pages.registration.business_plus_registration import BusinessPluss
from Pages.registration.guerilla_mail import GuerrillaMailPage,EmailInboxPage
from Pages.registration.Individual_registration_page import RegistrationPage



def test_individual_signup(driver_setup):
    driver = driver_setup

    guerrilla_mail_page = GuerrillaMailPage(driver)
    business_plus_user = BusinessPluss(driver)
    individual_user = RegistrationPage(driver)
    email_inbox_page = EmailInboxPage(driver)

    # opening new guerrilla mail to get new email address
    driver.get("https://www.guerrillamail.com/")
    email_address = guerrilla_mail_page.get_email_address()
    driver.maximize_window()

    # Opening Yoogo application in new tab
    business_plus_user.business_plus_registration(email_address, driver)

    # Back to guerrilla email to fetch the OTP and then authenticate the user.
    email_inbox_page.wait_for_email_list()
    email_inbox_page.click_verification_email()
    otp_digits = email_inbox_page.copy_otp()
    individual_user.authenticating_user(otp_digits)

#     Payment screen
    business_plus_user.business_plus_payment(driver)
    time.sleep(15)

