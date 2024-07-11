import time

from selenium.webdriver import Keys

from Resources.registration_data import RegistrationTestData
from Resources.business_registration_data import business_registrationTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import Config
from Pages.userprofile.registration.Individual_registration_page import RegistrationPage

from Utils.registration_locators import registrationLocators
from Utils.businessbasic_registration_locators import busniness_registrationLocators


class BusinessBasicRegistration:
    payment_processing: object

    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(registrationLocators.signup_button))
        signup_button.click()

    time.sleep(3)

    def select_business_basic_option(self):
        business_basic_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.business_basic_option))
        business_basic_option.click()



    def add_business(self):
        business_dropdown = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.business_basic_dropdown))
        business_dropdown.send_keys("code")
        add_business = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.addBusinessBtn))
        add_business.click()
        enter_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.email_input_field))
        enter_email.send_keys(business_registrationTestData.business_email)
        enter_company_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.company_name_input_field))
        enter_company_name.send_keys(business_registrationTestData.business_name)
        enter_business_url = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.business_url))
        enter_business_url.send_keys(business_registrationTestData.business_url)
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        country_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(busniness_registrationLocators.country_dropdown))
        country_dropdown.click()
        time.sleep(5)
        country_dropdown.send_keys(business_registrationTestData.country_name)
        country_dropdown.send_keys(Keys.ENTER)
        state_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown))
        state_dropdown.click()
        state_dropdown_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown_option))
        state_dropdown_option.click()
        city_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.city_input_field))
        city_name.click()
        city_name.send_keys(business_registrationTestData.city_name)
        postal_code = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.postalcode_input_field))
        postal_code.click()
        postal_code.send_keys(business_registrationTestData.postalcode)
        street_address = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.street_address_input_field))
        street_address.click()
        street_address.send_keys(business_registrationTestData.street_address)
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()

        revenue_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.revenue_input_field))
        revenue_input.send_keys(business_registrationTestData.revenue)
        company_size = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.company_size_input_field))
        company_size.send_keys(business_registrationTestData.company_size)
        ownership_type_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_dropdown))
        ownership_type_dropdown.click()
        ownership_type_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_option))
        ownership_type_option.click()
        entity_type_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(busniness_registrationLocators.entity_type_dropdown))
        entity_type_dropdown.click()
        entity_type_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.entity_type_option))
        entity_type_option.click()
        time.sleep(2)
        founded_year_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.founded_year_dropdown))
        founded_year_dropdown.click()
        founded_year_option = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(busniness_registrationLocators.founded_year_option))
        founded_year_option.click()
        time.sleep(2)
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        time.sleep(3)
        primary_industry_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.browse_button))
        primary_industry_button.click()
        primary_industry_parent_option = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_parent_option))
        primary_industry_parent_option.click()
        primary_industry_child_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option))
        primary_industry_child_option.click()
        primary_industry_child_option_1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option_1))
        primary_industry_child_option_1.click()
        primary_industry_child_option_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option_2))
        primary_industry_child_option_2.click()
        primary_industry_done = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.done_button))
        primary_industry_done.click()
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()

        add_business = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.add_business))
        add_business.click()

    def continue_button_click(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(registrationLocators.continue_button))
        continue_button.click()

    def enter_email(self, email_address):  # Corrected method signature here
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys(email_address)  # Corrected parameter name here

    def click_checkbox(self):
        checkbox_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.checkbox_1))
        checkbox_1.click()

    def personal_info(self):
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.name_text))
        name.send_keys(RegistrationTestData.username)
        surname = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.surname_text))
        surname.send_keys(RegistrationTestData.surname)
        password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(registrationLocators.newPassword_text))
        password.send_keys(RegistrationTestData.password)
        repeat_password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(registrationLocators.repeatPassword_text))
        repeat_password.send_keys(RegistrationTestData.password)

    def job_title(self):
        jobTitle_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(busniness_registrationLocators.jobTitle_dropdown))
        jobTitle_dropdown.click()
        jobTitle_option = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(busniness_registrationLocators.jobTitle_option))
        jobTitle_option.click()
        start_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.startDate_field))
        start_date.click()
        start_date_select = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(busniness_registrationLocators.startDate_option))
        start_date_select.click()

    def create_account_button(self):
        create_account_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(registrationLocators.create_account_button))
        create_account_button.click()

    def otp(self, otp_digits):
        signup_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(registrationLocators.otp_text_1))
        signup_button.send_keys(otp_digits)
    def job_title(self):
        job_title_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.jobTitle_input))
        job_title_dropdown.click()
        job_title_dropdown.send_keys(RegistrationTestData.Job_title)


        start_date = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(registrationLocators.start_date))
        start_date.click()
        start_date_year = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(registrationLocators.start_date_year))
        start_date_year.click()
        start_month = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(registrationLocators.start_month))
        start_month.click()

    def signup_basic_business(self, driver):
        isinstance_registration = RegistrationPage(driver)
        isinstance_registration.click_signup_button()
        self.select_business_basic_option()
        isinstance_registration.click_continue_button()
        self.add_business()
        isinstance_registration.click_continue_button()
        isinstance_registration.enter_email()
        isinstance_registration.click_checkbox()
        isinstance_registration.click_continue_button()
        isinstance_registration.personal_info()
        isinstance_registration.click_continue_button()
        self.job_title()
        isinstance_registration.click_continue_button()
        isinstance_registration.select_topic()
        isinstance_registration.click_continue_button()
        isinstance_registration.select_address()
        isinstance_registration.create_account_button()
        isinstance_registration.otp()
        isinstance_registration.click_continue_button()
        time.sleep(15)

