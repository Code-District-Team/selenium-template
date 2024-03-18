from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.email&passwordLocators import email&passwordLocators
from selenium.webdriver.support import expected_conditions as EC
class email_change:
    def __init__(self, driver):
        self.driver = driver
    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))


