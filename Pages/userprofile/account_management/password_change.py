import time

from Utils.change_email_passwordLocators import email_password_locators
from Resources.loginData import loginTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.changepassword_data import email_password_change_data
from faker import Faker

from Utils.profile_locators import profileLocators

faker = Faker()


class password_change:
    newPassword = None

    def __init__(self, driver):
        self.driver = driver

    def change_password_button(self):
        change_password_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.change_password_button))
        change_password_button.click()

    def enter_old_password(self, password):
        old_password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.old_password_field))
        old_password_field.click()
        old_password_field.send_keys(password)
        print("Old Password: " + password)

    def enter_new_password(self):
        new_password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.new_password_field))
        new_password_field.click()
        newPassword = faker.password()
        new_password_field.send_keys(newPassword)
        print("New Password: " + newPassword)
        return newPassword

    def repeat_new_password(self, newPass):
        repeat_password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.repeat_password_filed))
        repeat_password_field.click()
        repeat_password_field.send_keys(newPass)
        print("ReEnter Password: " + newPass)

    def save_password(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.save_button))
        save_button.click()
        time.sleep(3)

    def change_password(self, password):
        self.change_password_button()
        self.enter_old_password(password)
        newPass = self.enter_new_password()
        self.repeat_new_password(newPass)
        self.save_password()

        PasswordChangeToast_alert = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(profileLocators.businessAlert))
        actual_PasswordChangeToast_text = PasswordChangeToast_alert .text
        expected_PasswordChangeToast_text = "Password updated successfully"
        assert actual_PasswordChangeToast_text == expected_PasswordChangeToast_text, f"Expected '{expected_PasswordChangeToast_text}', but got '{actual_PasswordChangeToast_text }'"

        return newPass