import time

from selenium.webdriver import Keys

from Resources.registration_data import RegistrationTestData
from Resources.business_registration_data import buisness_registrationTestData

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Utils.registration_locators import registrationLocators
from Utils.businessbasic_registration_locators import busniness_registrationLocators
class business_basic_registration:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.signup_button))
        signup_button.click()
    time.sleep(3)
    def select_business_basic_option(self):
        business_basic_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.business_basic_option))
        business_basic_option.click()
    def click_continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.Continue_3_button))
        continue_button.click()
    def add_business(self,):
        business_dropdown = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.business_basic_dropdown))
        business_dropdown.click()
        add_business = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.add_business_select))
        add_business.click()
        enter_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.email_input_field))
        enter_email.send_keys(buisness_registrationTestData.business_email)
        enter_company_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.company_name_input_field))
        enter_company_name.send_keys(buisness_registrationTestData.business_name)
        enter_business_unit_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.business_division_name))
        enter_business_unit_name.send_keys(buisness_registrationTestData.business_unit_name)
        enter_business_url = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.business_url))
        enter_business_url.send_keys(buisness_registrationTestData.business_url)
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        time.sleep(2)
        country_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(busniness_registrationLocators.country_dropdown))
        country_dropdown.click()
        country_dropdown.send_keys(buisness_registrationTestData.country_name)
        country_dropdown.send_keys(Keys.ENTER)
        state_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown))
        state_dropdown.click()
        state_dropdown_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown_option))
        state_dropdown_option.click()
        city_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.city_input_field))
        city_name.send_keys(buisness_registrationTestData.city_name)
        postal_code = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.postalcode_input_field))
        postal_code.send_keys(buisness_registrationTestData.postalcode)
        street_address = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.street_address_input_field))
        street_address.send_keys(buisness_registrationTestData.street_address)
        time.sleep(50)
        continue_button_1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button_1))
        continue_button_1.click()
        time.sleep(2)
        revenue_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.revenue_input_field))
        revenue_input.send_keys(buisness_registrationTestData.revenue)
        company_size = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.company_size_input_field))
        company_size.send_keys(buisness_registrationTestData.company_size)
        entity_type_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.entity_type_dropdown))
        entity_type_dropdown.click()
        entity_type_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.entity_type_option))
        entity_type_option.click()
        founded_year_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.founded_year_option))
        founded_year_dropdown.click()
        founded_year_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.founded_year_option))
        founded_year_option.click()
        continue_button_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button_2))
        continue_button_2.click()
        time.sleep(3)
        primary_industry_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.browse_button))
        primary_industry_button.click()
        primary_industry_parent_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_parent_option))
        primary_industry_parent_option.click()
        primary_industry_child_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option))
        primary_industry_child_option.click()
        primary_industry_child_option_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option_1))
        primary_industry_child_option_1.click()
        primary_industry_child_option_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option_2))
        primary_industry_child_option_2.click()
        primary_industry_done = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.done_button))
        primary_industry_done.click()
        continue_button_3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button_3))
        continue_button_3.click()
        time.sleep(3)
        secondary_button_browse = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.browse_button))
        secondary_button_browse.click()
        secondary_industry_parent = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.secondary_industry_parent))
        secondary_industry_parent.click()
        secondary_industry_child = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.secondary_industry_child))
        secondary_industry_child.click()
        secondary_industry_child_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.secondary_industry_child_1))
        secondary_industry_child_1.click()
        secondary_industry_child_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.secondary_industry_child_2))
        secondary_industry_child_2.click()
        secondary_industry_done = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.done_button))
        secondary_industry_done.click()
        add_business = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.add_business_button))
        add_business.click()
    def continue_button_click(self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button_4))
        continue_button.click()
    def enter_email(self):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys(buisness_registrationTestData.basic_user_email)
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
        jobTitle_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(registrationLocators.jobTitle_dropdown))
        jobTitle_dropdown.click()
        jobTitle_option = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(registrationLocators.jobTitle_freelance))
        jobTitle_option.click()
        time.sleep(3)
        same_as_privious = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.same_as_previous_checkbox))
        same_as_privious.click()
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
        create_account_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.create_basic_business_account_button))
        create_account_button.click()
    def signup_basic_business(self):
        self.click_signup_button()
        time.sleep(2)
        self.select_business_basic_option()
        time.sleep(2)
        self.click_continue_button()
        time.sleep(2)
        self.add_business()
        time.sleep(2)
        self.enter_email()
        time.sleep(2)
        self.click_checkbox()
        time.sleep(2)
        self.personal_info()
        time.sleep(3)
        self.job_title()
        time.sleep(3)
        self.select_topic()
        time.sleep(3)
        self.select_address()
        time.sleep(3)
        self.create_account_button()
        time.sleep(5)























