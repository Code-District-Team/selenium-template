import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.userprofile.Registration.payment_page import PaymentPage
from Pages.userprofile.account_management.upgrade_individual_to_busines_plus import Subscription_upgrade_individual_to_business_plus
from Pages.userprofile.account_management.subscription_upgrade_individual_to_freelance import Subscription_upgrade_individual_to_freelance
from Pages.userprofile.account_management.subscription_downgrade_business_plus_to_business_basic import Subscription_downgrade_business_plus_to_business_basic
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
    def verfiy_subscription(self):
        currentSubscription = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Subscriptionupgradelocators.currentSubscription))
        currentSubscription = currentSubscription.text
        print(currentSubscription)
        if currentSubscription == "Business Plus":
            print("Subscription changes for Business Basic to Business plus successfully")
        else:
            print("Subscription not changed successfully")



    def upgrade_to_business_plus(self, driver_setup):
        self.navigate_to_subscription_tab()
        self.click_to_upgrade_business_plus()
        increase_seats = Subscription_upgrade_individual_to_business_plus(driver_setup)
        increase_seats.increase_seat_number()
        time.sleep(5)
        self.click_continue_to_payment()
        subscription_payment = PaymentPage(driver_setup)
        subscription_payment.payment_processing()
        isinstance_subscription = Subscription_upgrade_individual_to_business_plus(driver_setup)
        isinstance_subscription.click_to_continue()
        time.sleep(5)
        closePopup = Subscription_upgrade_individual_to_freelance(driver_setup)
        closePopup.close_popup()
        time.sleep(5)
        closeOnboardingModal = Subscription_downgrade_business_plus_to_business_basic(driver_setup)
        closeOnboardingModal.close_onboarding_model()

        self.navigate_to_subscription_tab()
        self.verfiy_subscription()



