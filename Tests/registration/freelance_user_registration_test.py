import time

from config import Config
from Pages.userprofile.Registration.freerlance_registration_page import freelance_registration
from Pages.userprofile.Registration.guerilla_mail import GuerrillaMailPage,EmailInboxPage




def test_freelance_signup(driver_setup):
    driver = driver_setup
    guerrilla_mail_page = GuerrillaMailPage(driver)
    freelance_user = freelance_registration(driver)
    email_inbox_page = EmailInboxPage(driver)
    driver.get("https://www.guerrillamail.com/")
    email_address = guerrilla_mail_page.get_email_address()
    driver.maximize_window()
    freelance_user.signup_freelance(driver, email_address)
    email_inbox_page.wait_for_email_list()
    email_inbox_page.click_verification_email()
    otp_digits = email_inbox_page.copy_otp()
    freelance_user.authenticating_user(otp_digits)
    freelance_user.freelance_payment(driver)
    time.sleep(15)

