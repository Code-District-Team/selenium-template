from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.registration_locators import registrationLocators
from Resources.registration_data import RegistrationTestData
from Pages.registration.guerilla_mail import GuerrillaMailPage,EmailInboxPage
from selenium.webdriver.support import expected_conditions as EC
from config import Config

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver



    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.signup_button))
        signup_button.click()
        self.driver.maximize_window()

    def click_continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.continue_button))
        continue_button.click()

    def enter_email(self, email_address):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys(email_address)

    def click_checkbox(self):
        checkbox_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.checkbox_1))
        checkbox_1.click()

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
        job_title_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.jobTitle_dropdown))
        job_title_dropdown.click()
        job_title_option = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(registrationLocators.jobTitle_dropdownitle_option))
        job_title_option.click()
        workplace_dropdown = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(registrationLocators.workplace_dropdown))
        workplace_dropdown.send_keys(RegistrationTestData.freelance_company)
        workplace_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.workplace_option))
        workplace_option.click()
        start_date = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.start_date))
        start_date.click()
        start_date_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.start_date_select))
        start_date_select.click()

    def select_topic(self):
        topics_browse = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.browse_button))
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
        create_account_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.create_account_button))
        create_account_button.click()

    def otp(self, otp_digits):
        signup_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.otp_text_1))
        # self.driver.execute_script("arguments[0].value = arguments[1];", signup_button, otp_digits)
        # # signup_button.send_keys(Keys.CONTROL + "v")
        signup_button.send_keys(otp_digits)

    def Verify_account(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(registrationLocators.verify_account))





    def individual_user_signup(self, email_address):
        original_window_handle = self.driver.current_window_handle
        self.driver.execute_script("window.open('" + Config.base_url + "', 'new window')")

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click_signup_button()
        self.click_continue_button()
        self.enter_email(email_address)
        self.click_checkbox()
        self.click_continue_button()
        self.personal_info()
        self.click_continue_button()
        self.job_title()
        self.click_continue_button()
        self.select_topic()
        time.sleep(5)
        self.click_continue_button()
        self.select_address()
        self.create_account_button()
        self.driver.switch_to.window(original_window_handle)
        self.driver.refresh()

    def authenticating_user(self, otp_digits):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.otp(otp_digits)
        self.click_continue_button()
        time.sleep(5)


