import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.MyNetwork.mynetwork import NetworkPage

from Pages.userprofile.Registration.payment_page import PaymentPage
from Pages.userprofile.Registration.freerlance_registration_page import FreelanceRegistration
from Utils.mynetwork_locators import mynetworkLocators
class Subscription_upgrade_individual_to_freelance:
    def __init__(self, driver):
        self.driver = driver
    def click_to_profile_icon(self):
        profileAvtar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.profileAvtar))
        profileAvtar.click()
    def click_to_account_settings(self):
        accountSettings = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Subscriptionupgradelocators.account_settings_tab))
        accountSettings.click()
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
    def close_popup(self):
        closeButton = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.closeButton))
        closeButton.click()
    def verify_subscription(self):
        self.half_page_scroll()
        currentSubscription = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Subscriptionupgradelocators.currentSubscription))
        currentSubscription = currentSubscription.text
        print(currentSubscription)
        if currentSubscription == "Freelancer":
            print("Subscription changes for individual to Freelance successfully")
        else:
            print("Subscription not changed successfully")
    def half_page_scroll(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        half_height = total_height / 2
        self.driver.execute_script(f"window.scrollTo(0, {half_height});")

    def upgrade_subcription_indvidual_to_free_lance(self, driver):
        self.click_to_profile_icon()
        self.click_to_account_settings()
        self.navigate_to_subscription_tab()
        self.half_page_scroll()
        self.click_to_upgrade_freelance()
        time.sleep(10)
        self.click_to_continue_button()
        time.sleep(5)
        self.click_to_continue_button()
        self.click_to_next()
        freelance_info = FreelanceRegistration(driver)
        freelance_info.freelance_info()
        self.continue_button()
        self.click_to_continue_button()
        subscription_payment = PaymentPage(driver)
        subscription_payment.payment_processing()
        self.click_to_continue_button()
        time.sleep(10)
        self.close_popup()
        self.navigate_to_subscription_tab()
        self.verify_subscription()
