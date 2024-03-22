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
from Utils.payment_locators import payment_page_locators
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
        Continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.Continue_3_button))
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
        mimum_projecct_size = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.minimum_project_size))
        mimum_projecct_size.send_keys(RegistrationTestData.minmum_project_price)
        availability_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.availability_dropdown))
        availability_dropdown.click()
        select_availablity = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.select_availability))
        select_availablity.click()
    def personal_info(self):
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.name_text))
        name.send_keys(RegistrationTestData.username)
        surname = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.surname_text))
        surname.send_keys(RegistrationTestData.surname)
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.newPassword_text))
        password.send_keys(RegistrationTestData.password)
        repeat_password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.repeatPassword_text))
        repeat_password.send_keys(RegistrationTestData.password)
    def job_title(self):
        jobTitle_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(registrationLocators.jobTitle_dropdown))
        jobTitle_dropdown.click()
        jobTitle_option = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(registrationLocators.jobTitle_freelance))
        jobTitle_option.click()
        time.sleep(3)
        workplace_dropdown = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(registrationLocators.workplace_freelance_dropdown))
        workplace_dropdown.send_keys(RegistrationTestData.freelance_company)
        workplace_option = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(registrationLocators.workplace_freelance_option))
        workplace_option.click()
        start_date = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.start_date_freelance))
        start_date.click()
        time.sleep(3)
        start_date_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.start_date_select))
        start_date_select.click()

    def select_topic(self):
        topics_browse = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.topics_browse))
        topics_browse.click()
        select_topic_primary = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.select_topic_primary))
        select_topic_primary.click()
        select_topic_2nd_tree = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.select_topic_2nd_tree))
        select_topic_2nd_tree.click()
        checked_box_for_topics = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.checked_box_for_topics))
        checked_box_for_topics.click()
        Done_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.Done_button))
        Done_button.click()
    def select_address(self):
        country_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.country_dropdown))
        country_dropdown.click()
        select_country = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.select_country))
        select_country.click()
        time.sleep(1)
        state_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.state_dropdown))
        state_dropdown.click()
        time.sleep(1)
        select_state = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.select_state))
        select_state.click()
        time.sleep(1)
        city_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.city_text))
        city_text.send_keys(RegistrationTestData.address)
        zipcode_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.zipcode_text))
        zipcode_text.send_keys(RegistrationTestData.zipcode)
        street_address_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.street_address_text))
        street_address_text.send_keys(RegistrationTestData.street_address)
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
        time.sleep(2)
        self.select_freelance_option()
        time.sleep(2)
        self.click_continue_button()
        time.sleep(2)
        self.enter_email(email_address)
        time.sleep(2)
        self.click_checkbox()
        time.sleep(2)
        self.click_continue_button()
        self.freelance_info()
        time.sleep(2)
        self.click_continue_button()
        self.personal_info()
        time.sleep(2)
        self.click_continue_button()
        self.job_title()
        self.click_continue_button()
        self.select_topic()
        self.click_continue_button()
        time.sleep(2)
        self.select_address()
        time.sleep(2)
        self.create_account_button()
        time.sleep(5)
        driver.switch_to.window(original_window_handle)
        driver.refresh()
        time.sleep(3)

    def authenticating_user(self, otp_digits):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.otp(otp_digits)
        time.sleep(5)
        self.continue_to_payment()

    def freelance_payment(self, driver):
        freelance_payment = payment_processing(driver)
        freelance_payment.payment_processing()

