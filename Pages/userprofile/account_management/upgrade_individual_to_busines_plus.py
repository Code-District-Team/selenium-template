import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.userprofile.registration.payment_page import PaymentPage
from Pages.userprofile.account_management.subscription_upgrade_individual_business_basic import Subscription_upgrade_individual_to_business_basic
from Pages.userprofile.registration.Individual_registration_page import RegistrationPage


class Subscription_upgrade_individual_to_business_plus:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_subscription_tab(self):
        subscription_tab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.subscription_tab))
        subscription_tab.click()

    def click_to_upgrade_business_plus(self):
        upgrade_to_business_basic_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_business_plus))
        upgrade_to_business_basic_button.click()
    def click_to_continue(self):
        click_to_continue = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.continue_button))
        click_to_continue.click()

    def increase_number_of_seats(self):
        increase_seat_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Subscriptionupgradelocators.seat_increase_button))
        increase_seat_button.click()

    def click_to_continue_to_increase_seat(self):
        continue_to_increase_seat_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Subscriptionupgradelocators.continue_to_increase_seat))
        continue_to_increase_seat_button.click()

    def increase_seat_number(self):
        increase_seats_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.seat_increase_button))
        increase_seats_button.click()

    def continue_to_payment(self):
        continue_to_payment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.continue_to_payment_button))
        continue_to_payment.click()

    def upgrade_to_business_plus(self, driver_setup):
        self.navigate_to_subscription_tab()
        self.click_to_upgrade_business_plus()
        click_to_add_business_field = Subscription_upgrade_individual_to_business_basic(driver_setup)
        click_to_add_business_field.click_to_add_business_field()
        add_business = Subscription_upgrade_individual_to_business_basic(driver_setup)
        add_business.add_new_business()
        time.sleep(5)
        self.click_to_continue()
        self.click_to_continue()
        self.click_to_continue()
        next_button = RegistrationPage(driver_setup)
        next_button.create_account_button()
        time.sleep(5)
        self.increase_seat_number()
        time.sleep(5)
        continue_button = RegistrationPage(driver_setup)
        continue_button.click_continue_button()
        subscription_payment = PaymentPage(driver_setup)
        subscription_payment.payment_processing()
