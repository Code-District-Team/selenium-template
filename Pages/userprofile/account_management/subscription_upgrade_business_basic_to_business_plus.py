import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.userprofile.account_management.upgrade_individual_to_busines_plus import Subscription_upgrade_individual_to_business_plus
from Pages.userprofile.registration.payment_page import payment_processing
class Subscription_upgrade_business_basic_to_business_plus:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_subscription_tab(self):
        subscription_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.subscription_tab))
        subscription_tab.click()
    def click_to_upgrade_business_plus(self):
        upgrade_to_business_plus_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_business_plus))
        upgrade_to_business_plus_button.click()
    def click_continue_to_payment(self):
        click_to_continue = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.continue_button))
        click_to_continue.click()


    def upgrade_to_business_plus(self, driver_setup):
        self.navigate_to_subscription_tab()
        self.click_to_upgrade_business_plus()
        increase_seats = Subscription_upgrade_individual_to_business_plus(driver_setup)
        increase_seats.increase_seat_number()
        time.sleep(10)
        self.click_continue_to_payment()

    def payment_for_subscription_upgrade(self, driver):
        subscription_payment = payment_processing(driver)
        subscription_payment.payment_processing()
