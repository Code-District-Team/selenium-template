from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.loginLocators import loginLocators
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located( loginLocators.email_textbox))
        email_field.send_keys(email)
        

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loginLocators.password_textbox))
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loginLocators.login_button))
        login_button.click()

    def email_error_message(self):
        time.sleep(1)
        email_error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loginLocators.login_error_message))
        assert email_error_message.text == "Please input your Email!", "Please input your Email!"
        time.sleep(1)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        time.sleep(3)

    def login_with_empty_fields(self,):
        self.click_login()
        time.sleep(3)
        email_error_message = self.wait_for_element_visibility(loginLocators.empty_email_field_error)
        print(email_error_message.text)
        expected_error_message = "Please enter your email."
        assert email_error_message.text == expected_error_message, f"Unexpected email error message: Expected '{expected_error_message}', Found '{email_error_message.text}'"

        time.sleep(3)
        password_error_message = self.wait_for_element_visibility(loginLocators.empty_password_field_error)
        assert password_error_message.text == "Please enter password", f"Unexpected password error message: {password_error_message.text}"
        time.sleep(1)
