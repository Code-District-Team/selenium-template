import time

from selenium.webdriver import Keys

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.userprofile.account_management.subscription_upgrade_individual_business_basic import Subscription_upgrade_individual_to_business_basic
from Pages.userprofile.account_management.subscription_upgrade_individual_to_freelance import Subscription_upgrade_individual_to_freelance
from Pages.userprofile.account_management.upgrade_individual_to_busines_plus import Subscription_upgrade_individual_to_business_plus
from Pages.userprofile.registration.payment_page import PaymentPage
class Subscription_upgrade_freelance_to_businessplus:
    def __init__(self, driver):
        self.driver = driver
    def click_upgrade_to_businessplus(self):
        upgrade_to_business_plus = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(Subscriptionupgradelocators.upgrade_to_business_plus))
        upgrade_to_business_plus.click()
    def verify_subscription(self):
        currentSubscription = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.currentSubscription))
        currentSubscription = currentSubscription.text
        print(currentSubscription)
        if currentSubscription == "BusinessPlus":
            print("Subscription changes for Freelance to Business Pluse successfully")
        else:
            print("Subscription not changed successfully")
    def freelance_to_businessplus(self, driver):

        navigate_to_subscription_tab = Subscription_upgrade_individual_to_freelance(driver)
        navigate_to_subscription_tab.navigate_to_subscription_tab()

        self.click_upgrade_to_businessplus()
        add_business_field = Subscription_upgrade_individual_to_business_basic(driver)
        add_business_field.click_to_add_business_field()
        add_business_field.add_new_business()
        add_business_field.click_to_continue()
        add_business_field.click_to_continue()
        add_business_field.click_to_continue()
        nextButton = Subscription_upgrade_individual_to_freelance(driver)
        nextButton.click_to_next()
        numberOfSeats = Subscription_upgrade_individual_to_business_plus(driver)
        numberOfSeats.increase_number_of_seats()
        add_business_field.click_to_continue()
        # paymentProcessing = payment_processing(driver)
        # paymentProcessing.payment_processing()
        time.sleep(5)
        self.verify_subscription()



