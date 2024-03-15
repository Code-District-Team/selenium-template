from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.registration_locators import registrationLocators
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver


    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.signup_button))
        signup_button.click()
        self.driver.maximize_window()

    def click_continue_button(self):
        Continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.Continue_button))
        Continue_button.click()

    def enter_email(self):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys("umer.ehsan+123@codedistrict.com")

    def click_checkbox(self):
        checkbox_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.checkbox_1))
        checkbox_1.click()

    def personal_info(self):
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.name_text))
        name.send_keys("umer")
        surname = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.surname_text))
        surname.send_keys("ehsan")
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.newPassword_text))
        password.send_keys("Code@4180")
        repeat_password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.repeatPassword_text))
        repeat_password.send_keys("Code@4180")

    def job_title(self):
        jobTitle_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.jobTitle_dropdown))
        jobTitle_dropdown.click()
        jobTitle_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.jobTitle_option))
        jobTitle_option.click()
        workplace_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.workplace_dropdown))
        workplace_dropdown.send_keys("Code")
        workplace_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.workplace_option))
        workplace_option.click()
        start_date = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.start_date))
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
        city_text.send_keys("Lahore")
        zipcode_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.zipcode_text))
        zipcode_text.send_keys("54000")
        street_address_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.street_address_text))
        street_address_text.send_keys("54000")

    def creat_account_button(self):
        create_account_button = WebDriverWait(self.driver, 10).until( EC.element_to_be_clickable(registrationLocators.create_account_button))
        create_account_button.click()



    def individual_user_signup(self):
        self.click_signup_button()
        self.click_continue_button()
        self.enter_email()
        self.click_checkbox()
        self.click_continue_button()
        self.personal_info()
        self.click_continue_button()
        self.job_title()
        self.click_continue_button()
        self.select_topic()
        self.click_continue_button()
        time.sleep(3)
        self.select_address()
        self.creat_account_button()
        time.sleep(3)
