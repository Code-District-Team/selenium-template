import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from Resources.loginData import loginTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.registration_data import RegistrationTestData
from Pages.registration.payment_page import payment_processing
class Subscription_upgrade_individual_to_freelance:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_subcription_tab(self):
        subscription_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.subscription_tab))
        subscription_tab.click()
    def click_to_upgrade_freelance(self):
        upgrade_to_freelance_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_freelance_button))
        upgrade_to_freelance_button.click()
    def freelance_info(self):
        description_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.description_text_box))
        description_text.click()
        description_text.send_keys("This is an automation text")
        hourly_rate = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.hourly_rate))
        hourly_rate.send_keys("10000")
        currency_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.currency_dropdown_field))
        currency_dropdown.click()
        select_currency_type = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.currency_dropdown_option))
        select_currency_type.click()
        minimum_project_size = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.minimum_project_size))
        minimum_project_size.send_keys(RegistrationTestData.minmum_project_price)
        availability_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.availability_dropdown))
        availability_dropdown.click()
        select_availability = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Subscriptionupgradelocators.availability_dropdown_option))
        select_availability.click()
    def click_to_continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.continue_button))
        continue_button.click()
    def upgrade_subscription_button(self):
        upgrade_subscription_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_subscription_button))
        upgrade_subscription_button.click()
    def upgrade_subcription_indvidual_to_free_lance(self):
        self.navigate_to_subcription_tab()
        self.click_to_upgrade_freelance()
        self.freelance_info()
        self.click_to_continue_button()
        time.sleep(5)
        self.click_to_continue_button()
        time.sleep(5)
        self.click_to_continue_button()
        time.sleep(5)
        self.upgrade_subscription_button()
    def payment_for_subscription_upgrade(self, driver):
        subscription_payment = payment_processing(driver)
        subscription_payment.payment_processing()
