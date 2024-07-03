
from Pages.userprofile.registration.businessbasic_registration import business_basic_registration
from Pages.userprofile.registration.guerilla_mail import GuerrillaMailPage,EmailInboxPage




def test_business_basic(driver_setup):
    driver = driver_setup
    guerrilla_mail_page = GuerrillaMailPage(driver)
    sigup_basic_business = business_basic_registration(driver)
    email_inbox_page = EmailInboxPage(driver)
    driver.get("https://www.guerrillamail.com/")
    email_address = guerrilla_mail_page.get_email_address()
    driver.maximize_window()
    sigup_basic_business.signup_basic_business(driver, email_address)
    email_inbox_page.wait_for_email_list()
    email_inbox_page.click_verification_email()
    otp_digits = email_inbox_page.copy_otp()
    sigup_basic_business.authenticating_user(otp_digits)
