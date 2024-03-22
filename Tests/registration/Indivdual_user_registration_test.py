from config import Config
from Pages.registration.Individual_registration_page import RegistrationPage
from Pages.registration.guerilla_mail import GuerrillaMailPage,EmailInboxPage



def test_individual_signup(driver_setup):
    driver = driver_setup

    guerrilla_mail_page = GuerrillaMailPage(driver)
    individual_user = RegistrationPage(driver)
    email_inbox_page = EmailInboxPage(driver)

    # opening new guerrilla mail to get new email address
    driver.get("https://www.guerrillamail.com/")
    email_address = guerrilla_mail_page.get_email_address()
    driver.maximize_window()

    # Opening Yoogo application in new tab
    individual_user.individual_user_signup(email_address)


    email_inbox_page.wait_for_email_list()
    email_inbox_page.click_verification_email()
    otp_digits = email_inbox_page.copy_otp()
    individual_user.authenticating_user(otp_digits)

