import os
import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Utils.onboardingLocators import onboardingLocators
from Resources.onboarding_data import onboardingTestData

class OnboardingPage:
    def __init__(self, driver: object) -> object:
        self.driver = driver

    def click_start_onboarding_button(self):
        self.wait_and_click(onboardingLocators.onboardingButton)

    def click_lets_complete_button(self):
        self.wait_and_click(onboardingLocators.letsCompleteButton)

    def upload_button(self):
        self.wait_and_click(onboardingLocators.imageUploadButton)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "profile.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(10)

    def next_button(self):
        next_button = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(onboardingLocators.nextButton))
        next_button.click()

    def page_assertion(self):
        page = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(onboardingLocators.page_assertion))
        assert page.text == "Please tell us more about yourself"

    def description_field(self):
        description_field = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.descriptionText))
        description_field.send_keys("testing")

    def update_button(self):
        self.wait_and_click(onboardingLocators.updateButton)

    def website_url(self):
        websiteText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.websiteText))
        websiteText.send_keys("https://www.codedistrict.com")

    def linkedIn_Url_Text(self):
        linkedInUrlText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.linkedInUrlText))
        linkedInUrlText.send_keys("https://www.linkedin.com/in/asadhafeez15")

    def twitter_Url_Text(self):
        twitterUrlText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.twitterUrlText))
        twitterUrlText.send_keys("https://x.com/asadhafeez_")

    def facebook_Url_Text(self):
        facebookUrlText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.facebookUrlText))
        facebookUrlText.send_keys("https://www.facebook.com/asad.hafeez.942/")

    def skip_verify(self):
        self.wait_and_click(onboardingLocators.skip_verify_account)

    def business_logo_upload(self):
        self.wait_and_click(onboardingLocators.imageUploadBusiness)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "images (1).jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(10)

    def next_button_1(self):
        self.wait_and_click(onboardingLocators.next_button_primary)

    def close_button(self):
        self.wait_and_click(onboardingLocators.closeButton)

    def tagline(self):
        tagline = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.tagline))
        tagline.send_keys("We are dreamers")
        time.sleep(40)

    def wait_and_click(self, locator):
        print(f"Waiting for element {locator} to be clickable...")
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        print(f"Element {locator} found. Clicking it now.")
        element.click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

    def onboarding_start(self):
        self.click_start_onboarding_button()
        time.sleep(5)
        self.click_lets_complete_button()
        time.sleep(3)
        self.upload_button()
        self.next_button()
        time.sleep(10)
        self.next_button()
        time.sleep(30)
        self.next_button()
        time.sleep(10)
        self.business_logo_upload()
        self.next_button()
        self.description_field()
        self.next_button()
        time.sleep(10)
        self.next_button()
        time.sleep(5)
        self.next_button_1()
        time.sleep(10)
        self.next_button()
        time.sleep(2)
        self.next_button()
        time.sleep(2)
        self.website_url()
        self.linkedIn_Url_Text()
        self.twitter_Url_Text()
        self.facebook_Url_Text()
        self.update_button()
        time.sleep(5)
        self.close_button()
        time.sleep(20)
