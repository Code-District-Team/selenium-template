import time

from Utils.account_status_locators import account_status_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AccountStatus:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

    def account_status_tab(self):
        account_status_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(account_status_locators.account_status_tab))
        account_status_tab.click()

    def account_suspend(self):
        account_suspend_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(account_status_locators.suspend_account_button))
        account_suspend_button.click()
        account_suspend_confirmation = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(account_status_locators.confirm_suspend_account_button))
        account_suspend_confirmation.click()
        status_message = self.wait_for_element_visibility(account_status_locators.account_status)
        expected_error_message = "Your Account has been Suspended"
        assert status_message.text == expected_error_message, f"Unexpected email error message: Expected '{expected_error_message}', Found '{status_message.text}'"

    def account_activation(self):
        account_activation_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(account_status_locators.suspend_account_button))
        account_activation_button.click()
        confirm_account_activation = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(account_status_locators.confirm_active_account_button))
        confirm_account_activation.click()
        status_message = self.wait_for_element_visibility(account_status_locators.account_status)
        expected_error_message = "Your Account has been activated"
        assert status_message.text == expected_error_message, f"Unexpected email error message: Expected '{expected_error_message}', Found '{status_message.text}'"

    def account_delete(self):
        account_delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(account_status_locators.delete_account_button))
        account_delete_button.click()
        confirm_account_delete = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(account_status_locators.confirm_delete_account_button))
        confirm_account_delete.click()


    def test_account_suspend_and_activation(self) -> object:
        self.account_status_tab()
        self.account_suspend()

    def test_account_delete(self):
        self.account_status_tab()
        self.account_delete()
