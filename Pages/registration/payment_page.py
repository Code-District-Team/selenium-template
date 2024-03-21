import time
from Resources.payment_data import payment_data

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Utils.payment_locators import payment_page_locators
class payment_processing:
    def __init__(self, driver):
        self.driver = driver
    def payment_processing(self):
        card_number = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(payment_page_locators.card_number_input_field))
        card_number.send_keys(payment_data.credit_card_number)
        expiry_date = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(payment_page_locators.expires_input_field))
        expiry_date.send_keys(payment_data.expiry_date)
        cvv_number = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(payment_page_locators.security_code_input_field))
        cvv_number.send_keys(payment_data.cvv_code)
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(payment_page_locators.continue_button))
        continue_button.click()
