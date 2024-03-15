from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.registration_locators import registrationLocators
from selenium.webdriver.support import expected_conditions as EC


class registrationPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        signup_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.signup_button))
        signup_button.click()

    def click_login(self):
        Continue_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registrationLocators.Continue_button))
        Continue_button.click()
    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located( registrationLocators.email_textbox))
        email_field.send_keys(email)
