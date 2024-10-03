import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

faker = Faker()

from selenium.webdriver.common.by import By



class email_password_locators:
    skip_onboarding = (By.ID, "verifyBtnSkip")
    emai_tab = (By.XPATH, "(//button[normalize-space()='Email & Password'])[1]")
    change_email_button = (By.ID, "change-email")
    new_email_field = (By.ID, "new-email")
    retype_email_field = (By.ID, "repeat-new-email")
    cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    change_password_button = (By.ID, "btnChangePassword")
    old_password_field = (By.NAME, "oldPassword")
    new_password_field = (By.NAME, "newPassword")
    repeat_password_filed = (By.NAME, "repeatNewPassword")
    save_button = (By.ID, "btn-save")
    businessAlert = (By.XPATH, "//div[@role='status']")
    profileAvtar = (By.XPATH, "//div[@id='profileAvatar']//*[name()='svg']")
    account_settings_tab = (By.XPATH, "//a[normalize-space()='Account Settings']")




class password_change:
    newPassword = None

    def __init__(self, driver):
        self.driver = driver
    def navigate_to_password_change_page(self):
        profileAvtar = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(email_password_locators.profileAvtar))
        profileAvtar.click()
        account_settings_tab = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(email_password_locators.account_settings_tab))
        account_settings_tab.click()




    def change_password_button(self):
        change_password_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(email_password_locators.change_password_button))
        change_password_button.click()

    def enter_old_password(self,password):
        old_password_field = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(email_password_locators.old_password_field))
        old_password_field.click()
        old_password_field.send_keys(password)
        print("Old Password: " + password)

    def enter_new_password(self):
        new_password_field = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(email_password_locators.new_password_field))
        new_password_field.click()
        newPassword = faker.password()
        new_password_field.send_keys(newPassword)
        print("New Password: " + newPassword)
        return newPassword

    def repeat_new_password(self, newPass):
        repeat_password_field = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(email_password_locators.repeat_password_filed))
        repeat_password_field.click()
        repeat_password_field.send_keys(newPass)
        print("ReEnter Password: " + newPass)

    def save_password(self):
        save_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(email_password_locators.save_button))
        save_button.click()
        time.sleep(3)

    def change_password(self, password):
        self.navigate_to_password_change_page()
        self.change_password_button()
        self.enter_old_password(password)
        newPass = self.enter_new_password()
        self.repeat_new_password(newPass)
        self.save_password()

        # PasswordChangeToast_alert = WebDriverWait(self.driver, 100).until(
        #     EC.visibility_of_element_located(email_password_locators.businessAlert))
        # actual_PasswordChangeToast_text = PasswordChangeToast_alert .text
        # expected_PasswordChangeToast_text = "Password updated successfully"
        # assert actual_PasswordChangeToast_text == expected_PasswordChangeToast_text, f"Expected '{expected_PasswordChangeToast_text}', but got '{actual_PasswordChangeToast_text }'"

        return newPass