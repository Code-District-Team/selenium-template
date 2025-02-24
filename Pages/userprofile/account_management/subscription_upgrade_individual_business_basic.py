import time

from selenium.webdriver import Keys

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from Utils.businessbasic_registration_locators import busniness_registrationLocators
from Resources.business_registration_data import business_registrationTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.userprofile.Registration.Individual_registration_page import RegistrationPage
from Pages.userprofile.account_management.subscription_upgrade_individual_to_freelance import Subscription_upgrade_individual_to_freelance
from Pages.userprofile.account_management.subscription_downgrade_business_plus_to_business_basic import Subscription_downgrade_business_plus_to_business_basic
class Subscription_upgrade_individual_to_business_basic:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_subcription_tab(self):
        subscription_tab = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.subscription_tab))
        subscription_tab.click()
    def click_to_upgrade_business_basic(self):
        upgrade_to_business_basic_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_business_basic))
        upgrade_to_business_basic_button.click()
    def click_to_add_business_field(self):
        add_business_field = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(Subscriptionupgradelocators.add_business_field))
        add_business_field.click()
        add_business_field.send_keys("co")
    def add_new_business(self):
        add_business_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.add_business_button))
        add_business_button.click()
        time.sleep(2)
        enter_email = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.email_input_field))
        enter_email.send_keys(business_registrationTestData.business_email)
        enter_company_name = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.company_name_input_field))
        enter_company_name.send_keys(business_registrationTestData.business_name)
        enter_business_url = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.business_url))
        enter_business_url.send_keys(business_registrationTestData.business_url)
        time.sleep(2)
        continue_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        country_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.country_dropdown))
        country_dropdown.click()
        time.sleep(3)
        country_dropdown.send_keys(business_registrationTestData.country_name)
        country_dropdown.send_keys(Keys.ENTER)
        state_dropdown = WebDriverWait(self.driver, 40).until( EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown))
        state_dropdown.click()
        state_dropdown_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown_option))
        state_dropdown_option.click()
        city_name = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.city_input_field))
        city_name.click()
        city_name.send_keys(business_registrationTestData.city_name)
        postal_code = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.postalcode_input_field))
        postal_code.click()
        postal_code.send_keys(business_registrationTestData.postalcode)
        street_address = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.street_address_input_field))
        street_address.click()
        street_address.send_keys(business_registrationTestData.street_address)
        continue_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        time.sleep(2)
        revenue_input = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.revenue_input_field))
        revenue_input.send_keys(business_registrationTestData.revenue)
        company_size = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.company_size_input_field))
        company_size.send_keys(business_registrationTestData.company_size)
        ownership_type_dropdown = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_dropdown))
        ownership_type_dropdown.click()
        ownership_type_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_option))
        ownership_type_option.click()
        entity_type_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(busniness_registrationLocators.entity_type_dropdown))
        entity_type_dropdown.click()
        entity_type_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.entity_type_option))
        entity_type_option.click()
        time.sleep(1)
        founded_year_dropdown = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.founded_year_dropdown))
        founded_year_dropdown.click()
        founded_year_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.founded_year_option))
        founded_year_option.click()
        time.sleep(1)
        continue_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        primary_industry_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.browse_button))
        primary_industry_button.click()
        primary_industry_parent_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.primary_industry_parent_option))
        primary_industry_parent_option.click()
        primary_industry_child_option = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.primary_industry_child_option))
        primary_industry_child_option.click()
        primary_industry_child_option_1 = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.primary_industry_child_option_1))
        primary_industry_child_option_1.click()
        time.sleep(1)
        primary_industry_child_option_2 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.primary_industry_child_option_2))
        primary_industry_child_option_2.click()
        primary_industry_done = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.done_button))
        primary_industry_done.click()
        continue_button = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        time.sleep(1)
        add_business = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.add_business))
        add_business.click()
    def click_to_continue(self):
        click_to_continue = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.continue_button_business))
        click_to_continue.click()
    def verify_subscription(self):
        self.half_page_scroll()
        currentSubscription = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.currentSubscription))
        currentSubscription = currentSubscription.text
        print(currentSubscription)
        if currentSubscription == "Business Basic":
            print("Subscription changes for individual to Business Basic successfully")
        else:
            print("Subscription not changed successfully")
    def half_page_scroll(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        half_height = total_height / 2
        self.driver.execute_script(f"window.scrollTo(0, {half_height});")
    def upgrade_to_business_basic(self, driver):
        self.navigate_to_subcription_tab()
        self.half_page_scroll()
        self.click_to_upgrade_business_basic()
        self.click_to_add_business_field()
        self.add_new_business()
        time.sleep(5)
        self.click_to_continue()
        self.click_to_continue()
        time.sleep(5)
        continue_button = RegistrationPage(driver)
        continue_button.click_continue_button()
        Next_button = RegistrationPage(driver)
        Next_button.create_account_button()
        closePopup = Subscription_upgrade_individual_to_freelance(driver)
        closePopup.close_popup()
        time.sleep(3)
        closeOnboardingModal = Subscription_downgrade_business_plus_to_business_basic(driver)
        closeOnboardingModal.close_onboarding_model()
        self.verify_subscription()


