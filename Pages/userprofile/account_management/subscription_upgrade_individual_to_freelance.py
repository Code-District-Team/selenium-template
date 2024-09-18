import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from Pages.userprofile.Registration.payment_page import PaymentPage
from Pages.userprofile.Registration.freerlance_registration_page import FreelanceRegistration


class SubscriptionUpgradeLocators:
    profileAvtar = (By.XPATH, "//div[@id='profileAvatar']//*[name()='svg']")
    account_settings_tab = (By.XPATH, "//a[normalize-space()='Account Settings']")
    subscription_tab = (By.XPATH, "//button[normalize-space()='Subscription']")
    upgrade_to_freelance_button = (By.XPATH, "(//button[normalize-space()='Upgrade to Freelancer'])[1]")
    button_continue = (By.XPATH, "//button[normalize-space()='Continue']")
    hourly_rate = (By.NAME, "hourlyRate")
    currency_dropdown_field = (By.XPATH, "//div[@id='mui-component-select-currency']")
    currency_dropdown_option = (By.XPATH, "//li[contains(text(),'Costa Rica Colon (₡)')]")
    minimum_project_size = (By.NAME, "minProjectSize")
    availability_dropdown = (By.ID, "mui-component-select-availability")
    availability_dropdown_option = (By.XPATH, "//li[normalize-space()='Full-Time']")
    continue_button = (By.ID, "regBtnContinue")
    chose_a_country_input = (By.ID, ":r1e:")
    state_field_dropdown = (By.ID, "mui-component-select-province")
    state_input_field_option = (By.XPATH, "//li[contains(text(),'Badakhshān (AF-BDS)')]")
    upgrade_subscription_button = (By.XPATH, "(//button[normalize-space()='Upgrade Subscription'])[1]")
    upgrade_to_business_basic = (By.XPATH, "(//button[normalize-space()='Upgrade to Business Basic'])[1]")
    upgrade_to_business_plus = (By.XPATH, "(//button[normalize-space()='Upgrade to Business Plus'])[1]")
    seat_increase_button = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium counter-icon mui-vubbuv'])[2]")
    click_to_continue = (By.ID, ":r12:")
    add_business_field = (By.XPATH, "//input[@class= 'MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused mui-1ev6tyo']")
    add_business_button = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 body1 mui-1w6h4uc']")
    country_dropdown = (By.XPATH, "/html[1]/body[1]/div[6]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    primary_industry_parent_option = (By.XPATH, "//h6[@class='MuiTypography-root MuiTypography-h6 mui-1mopw5e' and .//span[1][text()='P'] and .//span[3][text()='r'] and .//span[5][text()='o']]")
    primary_industry_child_option = (By.XPATH, "(//p[normalize-space()='Legal Services (4)'])[1]")
    primary_industry_child_option_1 = (By.XPATH, "(//p[normalize-space()='Offices of Lawyers'])[1]")
    primary_industry_child_option_2 = (By.XPATH, '(//span[normalize-space()="Attorneys\' offices"])[1]')
    continue_to_increase_seat = (By.ID, ":rf:")
    continue_button_business = (By.ID, "regBtnContinue")
    nextButton = (By.ID, "createAccount")
    closeButton = (By.XPATH, "//button[normalize-space()='Close']")
    currentSubscription = (By.XPATH, "//span[@class='MuiChip-label MuiChip-labelMedium mui-9iedg7']")
    downgradeToIndividual = (By.XPATH, "//button[contains(@class, 'MuiButton-outlinedPrimary') and text()='Downgrade to Individual']")
    confirmDowngrade = (By.XPATH, "//button[normalize-space()='Continue']")
    downgradeToBusinessBasic = (By.XPATH, "(//button[normalize-space()='Downgrade to Business Basic'])[1]")
    closeOnboardingModal = (By.XPATH, "//*[name()='path' and contains(@d,'M19 6.41 1')]")
class Subscription_upgrade_individual_to_freelance:
    def __init__(self, driver):
        self.driver = driver
    def click_to_profile_icon(self):
        profileAvtar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.profileAvtar))
        profileAvtar.click()
    def click_to_account_settings(self):
        accountSettings = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.account_settings_tab))
        accountSettings.click()
    def navigate_to_subscription_tab(self):
        time.sleep(5)
        subscription_tab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.subscription_tab))
        subscription_tab.click()
    def click_to_upgrade_freelance(self):
        upgrade_to_freelance_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.upgrade_to_freelance_button))
        upgrade_to_freelance_button.click()
    def continue_button (self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SubscriptionUpgradeLocators.button_continue))
        continue_button.click()

    def click_to_continue_button(self):
        continue_button = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.continue_button))
        continue_button.click()
    def upgrade_subscription_button(self):
        upgrade_subscription_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.upgrade_subscription_button))
        upgrade_subscription_button.click()
    def click_to_next(self):
        nextButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.nextButton))
        nextButton.click()
    def close_popup(self):
        closeButton = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.closeButton))
        closeButton.click()
    def verify_subscription(self):
        self.half_page_scroll()
        currentSubscription = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(SubscriptionUpgradeLocators.currentSubscription))
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
