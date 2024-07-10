import time

from selenium.webdriver.common.by import By

from Resources.payment_data import payment_data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utils.payment_locators import payment_page_locators
class payment_processing:
    def __init__(self, driver):
        self.driver = driver
    def payment_processing(self):
        # waiting for element to visible.
        continue_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Continue'])[1]")))
        # switching into iframes of card numer
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-number']")))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='number' and @id='credit-card-number']"))).send_keys("5555555555554444")
        # switching back to main frame
        self.driver.switch_to.default_content()

        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-expirationDate']")))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='expiration'])[1]"))).send_keys("11/2027")

        self.driver.switch_to.default_content()
        # switching into iframes of expiry date
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-cvv']")))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='cvv' and @id='cvv']"))).send_keys("456")
        # switching back to main frame
        self.driver.switch_to.default_content()
        continue_button.click()

