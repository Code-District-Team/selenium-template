import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from Resources.loginData import loginTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.registration_data import RegistrationTestData
from Pages.registration.payment_page import payment_processing
from Pages.registration.freerlance_registration_page import freelance_registration
class Subscription_upgrade_individual_to_freelance:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_subscription_tab(self):
        subscription_tab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.subscription_tab))
        subscription_tab.click()
    def click_to_upgrade_freelance(self):
        upgrade_to_freelance_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_freelance_button))
        upgrade_to_freelance_button.click()
    def continue_button (self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.button_continue))
        continue_button.click()

    def click_to_continue_button(self):
        continue_button = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(Subscriptionupgradelocators.continue_button))
        continue_button.click()
    def upgrade_subscription_button(self):
        upgrade_subscription_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_subscription_button))
        upgrade_subscription_button.click()
    def click_to_next(self):
        nextButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.nextButton))
        nextButton.click()
    def upgrade_subcription_indvidual_to_free_lance(self, driver):
        self.navigate_to_subscription_tab()
        self.click_to_upgrade_freelance()
        time.sleep(60)
        self.click_to_continue_button()
        self.click_to_continue_button()
        self.click_to_next()
        freelance_info = freelance_registration(driver)
        freelance_info.freelance_info()
        self.continue_button()
        self.click_to_continue_button()
    def payment_for_subscription_upgrade(self, driver):
        subscription_payment = payment_processing(driver)
        subscription_payment.payment_processing()
