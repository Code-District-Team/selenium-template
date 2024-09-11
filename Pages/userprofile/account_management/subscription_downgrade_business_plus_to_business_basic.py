import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.userprofile.account_management.subscription_upgrade_individual_to_freelance import Subscription_upgrade_individual_to_freelance
from Pages.userprofile.account_management.subscription_downgrade_freelance_individual import Subscription_downgrade_freelance_to_individual
class Subscription_downgrade_business_plus_to_business_basic:
    def __init__(self, driver):
        self.driver = driver
    def click_to_downgrade(self):
        businessPlusToIndividual = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.downgradeToBusinessBasic))
        businessPlusToIndividual.click()
    def close_onboarding_model(self):
        close_onboarding_model = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.closeOnboardingModal))
        close_onboarding_model.click()
    def verfiy_downgrade(self):
        self.half_page_scroll()
        currentSubscription = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Subscriptionupgradelocators.currentSubscription))
        currentSubscription = currentSubscription.text
        print(currentSubscription)
        if currentSubscription == "Business Basic":
            print("Subscription changes for Business plus to Business Basic successfully")
        else:
            print("Subscription not changed successfully")
    def half_page_scroll(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        half_height = total_height / 2
        self.driver.execute_script(f"window.scrollTo(0, {half_height});")


    def subscription_downgrade_business_plus_to_Business_plus(self, driver):
        navigate_to_subscription = Subscription_upgrade_individual_to_freelance(driver)
        navigate_to_subscription.click_to_profile_icon()
        navigate_to_subscription.click_to_account_settings()
        navigate_to_subscription.navigate_to_subscription_tab()

        self.half_page_scroll()
        self.click_to_downgrade()
        click_on_downgrade = Subscription_downgrade_freelance_to_individual(driver)
        click_on_downgrade.click_confirm_downgrade()
        navigate_to_subscription.close_popup()
        time.sleep(3)
        self.close_onboarding_model()
        self.half_page_scroll()
        self.verfiy_downgrade()
        time.sleep(5)

