import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.registration.payment_page import payment_processing
from Pages.account_management.subscription_upgrade_individual_business_basic import Subscription_upgrade_individual_to_business_basic


class Subscription_upgrade_individual_to_business_plus:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_subscription_tab(self):
        subscription_tab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.subscription_tab))
        subscription_tab.click()

    def click_to_upgrade_business_plus(self):
        upgrade_to_business_basic_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_business_plus))
        upgrade_to_business_basic_button.click()
    def add_new_business(self):
        add_business_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.add_business_button))
        add_business_button.click()
        time.sleep(2)
        enter_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.email_input_field))
        enter_email.send_keys(buisness_registrationTestData.business_email)
        enter_company_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.company_name_input_field))
        enter_company_name.send_keys(buisness_registrationTestData.business_name)
        enter_business_unit_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.business_division_name))
        enter_business_unit_name.send_keys(buisness_registrationTestData.business_unit_name)
        enter_business_url = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.business_url))
        enter_business_url.send_keys(buisness_registrationTestData.business_url)
        time.sleep(5)
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()

        country_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.country_dropdown))
        country_dropdown.click()
        country_dropdown.send_keys(buisness_registrationTestData.country_name)
        country_dropdown.send_keys(Keys.ENTER)
        state_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown))
        state_dropdown.click()
        state_dropdown_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown_option))
        state_dropdown_option.click()
        city_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.city_input_field))
        city_name.send_keys(buisness_registrationTestData.city_name)
        postal_code = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.postalcode_input_field))
        postal_code.send_keys(buisness_registrationTestData.postalcode)
        street_address = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.street_address_input_field))
        street_address.send_keys(buisness_registrationTestData.street_address)
        continue_button_1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.continue_button_1))
        continue_button_1.click()
        time.sleep(2)
        revenue_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.revenue_input_field))
        revenue_input.send_keys(buisness_registrationTestData.revenue)
        company_size = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.company_size_input_field))
        company_size.send_keys(buisness_registrationTestData.company_size)
        ownership_type_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_dropdown))
        ownership_type_dropdown.click()
        ownership_type_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_option))
        ownership_type_option.click()
        entity_type_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(busniness_registrationLocators.entity_type_dropdown))
        entity_type_dropdown.click()
        entity_type_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.entity_type_option))
        entity_type_option.click()
        time.sleep(2)
        founded_year_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.founded_year_dropdown))
        founded_year_dropdown.click()
        founded_year_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.founded_year_option))
        founded_year_option.click()
        time.sleep(2)
        continue_button_2 = WebDriverWait(self.driver, 0).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button_2))
        continue_button_2.click()
        primary_industry_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.primary_industry_browser))
        primary_industry_button.click()
        primary_industry_parent_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_parent_option))
        primary_industry_parent_option.click()
        primary_industry_child_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option))
        primary_industry_child_option.click()
        primary_industry_child_option_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option_1))
        primary_industry_child_option_1.click()
        time.sleep(5)
        primary_industry_child_option_2 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.primary_industry_option))
        primary_industry_child_option_2.click()
        primary_industry_done = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.done_button))
        primary_industry_done.click()
        continue_button_3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button_3))
        continue_button_3.click()
        time.sleep(3)
        secondary_button_browse = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.secondary_industry_browser))
        secondary_button_browse.click()
        secondary_industry_parent = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.secondary_industry_parent))
        secondary_industry_parent.click()
        secondary_industry_child = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.secondary_industry_child))
        secondary_industry_child.click()
        secondary_industry_child_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.secondary_industry_child_1))
        secondary_industry_child_1.click()
        secondary_industry_child_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.secondary_industry_option))
        secondary_industry_child_2.click()
        secondary_industry_done = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.done_button))
        secondary_industry_done.click()
        add_business = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(busniness_registrationLocators.add_business_button))
        add_business.click()

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
        time.sleep(30)
        click_to_add_business_field = Subscription_upgrade_individual_to_business_basic(driver_setup)
        click_to_add_business_field.click_to_add_business_field()
        add_business = Subscription_upgrade_individual_to_business_basic(driver_setup)
        add_business.add_new_business()
        time.sleep(40)
        self.click_to_continue_to_increase_seat()
        self.increase_seat_number()
        self.increase_seat_number()
        time.sleep(20)
        self.continue_to_payment()
    def payment_for_subscription_upgrade(self, driver):
        subscription_payment = payment_processing(driver)
        subscription_payment.payment_processing()
