from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.onboardingLocators import onboardingLocators
from Resources.onboarding_data import onboardingTestData
from selenium.webdriver.support import expected_conditions as EC

class OnboardingPage:
    def __init__(self, driver):
        self.driver = driver



    def click_start_onboarding_button(self):
        onboardingButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.onboardingButton))
        onboardingButton.click()


    def click_lets_complete_button(self):
        lets_complete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.letsCompleteButton))
        lets_complete_button.click()

    def upload_button(self):
        upload_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.imageUploadButton))
        upload_button.click()

    def next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.nextButton))
        next_button.click()

    def description_field(self):
        description_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.descriptionText))
        description_field.send_keys("testing")

    def update_button(self):
        update_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.updateButton))
        update_button.click()

    def website_url(self):
        websiteText = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.websiteText))
        websiteText.send_keys("https://www.codedistrict.com")

    def linkedIn_Url_Text(self):
        linkedInUrlText = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.linkedInUrlText))
        linkedInUrlText.send_keys("https://www.twitter.com")

    def twitter_Url_Text(self):
        twitterUrlText = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.twitterUrlText))
        twitterUrlText.send_keys("https://www.linkedin.com")

    def facebook_Url_Text(self):
        facebookUrlText = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(onboardingLocators.facebookUrlText))
        facebookUrlText.send_keys("https://www.facebook.com")


    def onboarding_start(self):
        self.click_start_onboarding_button()
        self.click_lets_complete_button()
        self.next_button()
        self.next_button()
        self.next_button()
        self.next_button()
        self.next_button()
        self.description_field()
        self.next_button()
        self.next_button()
        self.next_button()
        self.next_button()
        self.next_button()
        self.website_url()
        self.linkedIn_Url_Text()
        self.twitter_Url_Text()
        self.facebook_Url_Text()
        self.upload_button()
        time.sleep(5)



