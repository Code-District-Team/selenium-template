import time

from Utils.change_email_passwordLocators import email_password_locators
from Resources.loginData import loginTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.changepassword_data import email_password_change_data


class password_change:
    def __init__(self, driver):
        self.driver = driver


    def change_password_button(self):
        change_password_button  = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_password_locators.change_password_button))
        change_password_button.click()

    def enter_old_password(self, password = loginTestData.valid_credential["password"]):
        old_password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_password_locators.old_password_field))
        old_password_field.click()
        old_password_field.send_keys(password)

    def enter_new_password(self):
        new_password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_password_locators.new_password_field))
        new_password_field.click()
        new_password_field.send_keys(email_password_change_data.new_password)

    def repeat_new_password(self):
        repeat_password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_password_locators.repeat_password_filed))
        repeat_password_field.click()
        repeat_password_field.send_keys(email_password_change_data.repeat_password)
    def save_password(self):
        save_button= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_password_locators.save_button))
        save_button.click()
        time.sleep(3)




    def change_password(self, password: object = loginTestData.valid_credential["password"]) -> object:
        self.change_password_button()
        self.enter_old_password(password)
        self.enter_new_password()
        self.repeat_new_password()
        self.save_password()


