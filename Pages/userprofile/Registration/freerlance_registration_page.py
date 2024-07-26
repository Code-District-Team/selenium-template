import time
from Pages.userprofile.Registration.Individual_registration_page import RegistrationPage

from Resources.registration_data import RegistrationTestData
from Resources.payment_data import payment_data


from selenium.webdriver.support import expected_conditions as EC
from Pages.userprofile.Registration.payment_page import PaymentPage
from selenium.webdriver.support.ui import WebDriverWait
from Utils.registration_locators import registrationLocators
class FreelanceRegistration:
    def __init__(self, driver):
        self.driver = driver


    time.sleep(3)
    def select_freelance_option(self):
        freelance_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(registrationLocators.freelance_option))
        freelance_option.click()
    def enter_email(self):
        email_field = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys(RegistrationTestData.email)

    def freelance_info(self):
        description_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.description_box))
        description_text.click()
        description_text.send_keys("This is an automation text")
        hourly_rate = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.hourly_rate))
        hourly_rate.send_keys("10000")
        currency_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.currency_dropdown))
        currency_dropdown.click()
        select_currency_type = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.select_currency))
        select_currency_type.click()
        minimumProjectSize = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.minimum_project_size))
        minimumProjectSize.send_keys(RegistrationTestData.minimum_project_price)
        availability_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.availability_dropdown))
        availability_dropdown.click()
        select_availablity = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.select_availability))
        select_availablity.click()
    def click_to_continue(self):
        continue_button =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.continue_button_freelance))
        continue_button.click()
    def create_account_button(self):
        create_account_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.create_freelance_account_button))
        create_account_button.click()
    def otp(self, otp_digits):
        signup_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.otp_text_1))
        signup_button.send_keys(otp_digits)
    def continue_to_payment(self):
        continue_to_payment_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.continue_2_payment_screen))
        continue_to_payment_button.click()

    def enter_email(self):
        fake = Faker()
        uuid = RegistrationTestData.generate_uuid()
        email = f"{uuid}{fake.email()}"
        email_field = WebDriverWait(self.driver, 40).until(
        EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys(email)
        email = RegistrationTestData.email
        print(email)


    def signup_freelance(self, driver):
        isinstance_registration = RegistrationPage(self.driver)
        isinstance_registration.click_signup_button()
        self.select_freelance_option()
        isinstance_registration.click_continue_button()
        isinstance_registration.enter_email()
        isinstance_registration.click_checkbox()
        isinstance_registration.click_continue_button()
        isinstance_registration.personal_info()
        isinstance_registration.click_continue_button()
        isinstance_registration.job_title()
        isinstance_registration.click_continue_button()
        self.freelance_info()
        self.click_to_continue()
        isinstance_registration.select_topic()
        isinstance_registration.click_continue_button()
        isinstance_registration.select_address()
        isinstance_registration.create_account_button()
        isinstance_registration.otp()
        isinstance_registration.click_continue_button()
        freelance_payment = PaymentPage(driver)
        freelance_payment.payment_processing()
        isinstance_registration.click_continue_button()
        time.sleep(15)


