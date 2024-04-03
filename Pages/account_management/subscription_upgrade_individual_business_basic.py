import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.registration.businessbasic_registration import business_basic_registration
class Subscription_upgrade_individual_to_business_basic:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_subcription_tab(self):
        subscription_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.subscription_tab))
        subscription_tab.click()
    def click_to_upgrade_business_basic(self):
        upgrade_to_businessbasic_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_business_basic))
        upgrade_to_businessbasic_button.click()

    def upgrade_to_business_basic(self, driver_setup):
        self.navigate_to_subcription_tab()
        self.click_to_upgrade_business_basic()
        add_business = business_basic_registration(driver_setup)
        add_business.add_business()
