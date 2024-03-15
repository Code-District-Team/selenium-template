from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.registration_locators import registrationLocators
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.signup_button))
        signup_button.click()

    def click_continue_button(self):
        Continue_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.Continue_button))
        Continue_button.click()
    def enter_email(self):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys("umer.ehsan+123@codedistrict.com")

    def click_checkbox(self):
        checkbox_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.checkbox_1))
        checkbox_1.click()

    def click_continue_button(self):
        Continue_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.Continue_button))
        Continue_button.click()

    def enter_email(self, email)
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located( registrationLocators.email_textbox))
        email_field.send_keys(email)








    def individual_user_signup(self):
        self.click_signup_button()
        self.click_continue_button()
        self.enter_email()
        self.click_checkbox()
        self.click_continue_button()