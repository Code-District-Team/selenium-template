from selenium.webdriver.support.ui import WebDriverWait
import time
from Pages.userprofile.Registration.payment_page import PaymentPage
from Utils.registration_locators import registrationLocators
from Pages.userprofile.Registration.businessbasic_registration import BusinessBasicRegistration
from selenium.webdriver.support import expected_conditions as EC
from Pages.userprofile.Registration.Individual_registration_page import RegistrationPage


class BusinessPlus:

    def __init__(self, driver):
        self.driver = driver



    def select_business_account(self):
        business_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.business_plus_account))
        business_button.click()

    def add_seats(self):
        add_seats = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(registrationLocators.seats_button))
        add_seats.click()
        add_seats.click()
    def business_plus_signup(self, driver):
        isinstance_registration = RegistrationPage(driver)
        isinstance_registration.click_signup_button()
        self.select_business_account()
        isinstance_registration.click_continue_button()
        isinstance_businessbaisc = BusinessBasicRegistration(driver)
        isinstance_businessbaisc.add_business()
        isinstance_registration.click_continue_button()
        isinstance_registration.enter_email()
        isinstance_registration.click_checkbox()
        isinstance_registration.click_continue_button()
        isinstance_registration.personal_info()
        isinstance_registration.click_continue_button()
        isinstance_businessbaisc.job_title()
        isinstance_registration.click_continue_button()
        isinstance_registration.select_topic()
        isinstance_registration.click_continue_button()
        isinstance_registration.select_address()
        isinstance_registration.create_account_button()
        isinstance_registration.otp()
        isinstance_registration.click_continue_button()
        self.add_seats()
        isinstance_registration.click_continue_button()
        time.sleep(5)
        payment = PaymentPage(driver)
        payment.payment_processing()
        isinstance_registration.click_continue_button()
        time.sleep(4)
