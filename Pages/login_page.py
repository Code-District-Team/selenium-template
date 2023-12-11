from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.ID, 'loginForm_email')
        self.password_textbox = (By.ID, 'loginForm_password')
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.login_error_message = (By.XPATH, "//div[@class='ant-form-item-explain-error']")

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_textbox))
        email_field.send_keys(email)
        

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_textbox))
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button))
        login_button.click()

    def email_error_message(self):
        time.sleep(1)
        email_error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_error_message))
        assert email_error_message.text == "Please input your Email!", "Please input your Email!"
        time.sleep(1)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        time.sleep(3)
