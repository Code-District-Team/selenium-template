import time

from Utils.subscription_upgrade_locators import Subscriptionupgradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.userprofile.account_management.subscription_upgrade_individual_to_freelance import Subscription_upgrade_individual_to_freelance

class Subscription_downgrade_freelance_to_individual:
    def __init__(self, driver):
        self.driver = driver

    def click_to_downgrade(self):
        freelanceToIndividual = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.downgradeToIndividual))
        freelanceToIndividual.click()
    def click_confirm_downgrade(self):
        confirmDowngrade = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(Subscriptionupgradelocators.confirmDowngrade))
        confirmDowngrade.click()
    def verfiy_downgrade(self):
        self.half_page_scroll()
        currentSubscription = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Subscriptionupgradelocators.currentSubscription))
        currentSubscription = currentSubscription.text
        print(currentSubscription)
        if currentSubscription == "Individual":
            print("Subscription changes for Freelance to individual successfully")
        else:
            print("Subscription not changed successfully")
    def half_page_scroll(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        half_height = total_height / 2
        self.driver.execute_script(f"window.scrollTo(0, {half_height});")

    def downgrade_to_individual(self):
        isinstance_individual = Subscription_upgrade_individual_to_freelance(self.driver)
        isinstance_individual.click_to_profile_icon()
        isinstance_individual.click_to_account_settings()
        isinstance_individual.navigate_to_subscription_tab()
        time.sleep(1)
        self.click_to_downgrade()
        self.click_confirm_downgrade()
        isinstance_individual.close_popup()
        self.verfiy_downgrade()




