import os
import pyautogui
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
        onboardingButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.onboardingButton))
        onboardingButton.click()


    def click_lets_complete_button(self):
        lets_complete_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.letsCompleteButton))
        lets_complete_button.click()

    def upload_button(self):
        upload_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.imageUploadButton))
        upload_button.click()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "profile.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(7)


    def Topic_wait(self):
        Topic = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.Topics))

    def Primary_wait(self):
        Primary = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.Primary))

    def next_button(self):
        next_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.nextButton))
        next_button.click()

    def page_assertion(self):
        page = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.page_assertion))
        assert page.text == "Please tell us more about yourself"
        # next_button.click()

    def description_field(self):
        description_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.descriptionText))
        description_field.send_keys("testing")

    def update_button(self):
        update_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.updateButton))
        update_button.click()

    def website_url(self):
        websiteText = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.websiteText))
        websiteText.send_keys("https://www.codedistrict.com")

    def linkedIn_Url_Text(self):
        linkedInUrlText = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.linkedInUrlText))
        linkedInUrlText.send_keys("https://www.twitter.com")

    def twitter_Url_Text(self):
        twitterUrlText = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.twitterUrlText))
        twitterUrlText.send_keys("https://www.linkedin.com")

    def facebook_Url_Text(self):
        facebookUrlText = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.facebookUrlText))
        facebookUrlText.send_keys("https://www.facebook.com")

    def skip_verify(self):
        skip_verify_account = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(onboardingLocators.skip_verify_account))
        skip_verify_account.click()


    def onboarding_start(self):
        self.skip_verify()
        self.click_start_onboarding_button()
        time.sleep(5)
        self.click_lets_complete_button()
        time.sleep(3)
        self.upload_button()
        self.next_button()
        self.Topic_wait()
        self.Primary_wait()
        self.page_assertion()
        self.next_button()
        self.next_button()

        self.next_button()
        self.description_field()
        self.next_button()
        time.sleep(2)
        self.next_button()
        time.sleep(2)
        self.next_button()
        time.sleep(2)
        self.next_button()
        time.sleep(2)
        self.next_button()
        time.sleep(2)
        time.sleep(2)
        self.website_url()
        self.linkedIn_Url_Text()
        self.twitter_Url_Text()
        self.facebook_Url_Text()
        self.upload_button()
        time.sleep(5)



