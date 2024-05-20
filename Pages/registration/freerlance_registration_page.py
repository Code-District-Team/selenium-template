import time
from lib2to3.pgen2 import driver

from Resources.registration_data import RegistrationTestData
from Resources.payment_data import payment_data
from selenium.webdriver.common.by import By


from selenium.webdriver.support import expected_conditions as EC
from Pages.registration.payment_page import payment_processing
from selenium.webdriver.support.ui import WebDriverWait
from Utils.registration_locators import registrationLocators
from config import Config
from Pages.registration.Individual_registration_page import RegistrationPage
class freelance_registration:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.signup_button))
        signup_button.click()
        self.driver.maximize_window()
    time.sleep(3)
    def select_freelance_option(self):
        freelance_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.freelance_option))
        freelance_option.click()
    def click_continue_button(self):
        Continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.continue_button))
        Continue_button.click()
    def enter_email(self, email_address):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys(email_address)
    def click_checkbox(self):
        checkbox_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.checkbox_1))
        checkbox_1.click()
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
        minimumProjectsize = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.minimum_project_size))
        minimumProjectsize.send_keys(RegistrationTestData.minmum_project_price)
        availability_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.availability_dropdown))
        availability_dropdown.click()
        select_availablity = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.select_availability))
        select_availablity.click()
    def click_to_continue(self):
        continue_button = Continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.continue_button_freelance))
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


    def signup_freelance(self, driver, email_address):
        original_window_handle = driver.current_window_handle  # Corrected here
        self.driver.execute_script("window.open('" + Config.base_url + "', 'new window')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click_signup_button()
        self.select_freelance_option()
        self.click_continue_button()
        self.enter_email(email_address)
        self.click_checkbox()
        self.click_continue_button()
        personal_info = RegistrationPage(driver)
        personal_info.personal_info()
        self.click_continue_button()
        Job_title = RegistrationPage(driver)
        Job_title.job_title()
        self.click_continue_button()
        self.freelance_info()
        self.click_to_continue()
        area_of_interest = RegistrationPage(driver)
        area_of_interest.select_topic()
        time.sleep(20)
        self.click_continue_button()
        select_address = RegistrationPage(driver)
        select_address.select_address()
        create_account = RegistrationPage(driver)
        create_account.create_account_button()
        time.sleep(5)
        driver.switch_to.window(original_window_handle)
        driver.refresh()
        time.sleep(3)

    def authenticating_user(self, otp_digits):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.otp(otp_digits)
        time.sleep(10)
        self.click_continue_button()

    def freelance_payment(self, driver):
        freelance_payment = payment_processing(driver)
        freelance_payment.payment_processing()

