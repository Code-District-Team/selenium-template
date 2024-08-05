import os
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Utils.onboardingLocators import onboardingLocators
from Utils.profile_locators import profileLocators

class OnboardingPage:
    def __init__(self, driver):
        self.driver = driver

    def click_start_onboarding_button(self):
        self.wait_and_click(onboardingLocators.onboardingButton)

    def click_lets_complete_button(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(onboardingLocators.waitTextForLetsCompleteBtn))
        self.wait_and_click(onboardingLocators.letsCompleteButton)


    def upload_button(self):
        self.wait_and_click(onboardingLocators.imageUploadButton)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "profile.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(2)

    def next_button(self):
        next_button = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(onboardingLocators.nextButton))
        next_button.click()

    def page_assertion(self):
        page = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(onboardingLocators.page_assertion))
        assert page.text == "Please tell us more about yourself"

    def description_field(self):
        description_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.descriptionText))
        description_field.send_keys("testing")

    def businessSummary_field(self):
        time.sleep(2)
        revenue_field = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.revenueText))
        revenue_field.send_keys("400000")
        NoOfEmployees_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.noOfEmployeesText))
        NoOfEmployees_field.send_keys("200")
        ownership_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.ownerShipText))
        ownership_field.click()
        ownershipType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.ownerShipTypeText))
        ownershipType_field.click()
        entity_field = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.entityText))
        entity_field.click()
        entityType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.entityTypeText))
        entityType_field.click()
        headquaterText_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.headquaterText))
        headquaterText_field.click()
        headquaterType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.headquaterTypeText))
        headquaterType_field.click()
        foundedText_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.foundedText))
        foundedText_field.click()
        foundedType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.foundedTypeText))
        foundedType_field.click()

    def primaryIndustry_field(self):
        browse_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.browse_button))
        browse_field.click()
        browseOption_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.browseoption_btn))
        browseOption_field.click()

        subBrowseOption_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.subBrowseOption_btn))
        subBrowseOption_field.click()

        subBrowseOption_field_ = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.checkboxForPrimaryIndustry))
        subBrowseOption_field_.click()

        primaryIndustryChild_field_ = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.primaryChildText))
        primaryIndustryChild_field_.click()

        doneBtn_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.donebBtn))
        doneBtn_field.click()

    def update_button(self):
        self.wait_and_click(onboardingLocators.updateButton)
        time.sleep(2)

    def website_url(self):
        websiteText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.websiteText))
        websiteText.send_keys("https://www.codedistrict.com")

    def linkedIn_Url_Text(self):
        linkedInUrlText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.linkedInUrlText))
        linkedInUrlText.send_keys("https://www.linkedin.com/in/asadhafeez15")

    def twitter_Url_Text(self):
        twitterUrlText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.twitterUrlText))
        twitterUrlText.send_keys("https://x.com/asadhafeez_")

    def facebook_Url_Text(self):
        facebookUrlText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.facebookUrlText))
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
        time.sleep(2)

    def next_button_1(self):
        self.wait_and_click(onboardingLocators.next_button_primary)

    def close_button(self):
        self.wait_and_click(onboardingLocators.closeButton)

    def tagline(self):
        tagline = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.tagline))
        tagline.send_keys("We are dreamers")

    def wait_and_click(self, locator):
        print(f"Waiting for element {locator} to be clickable...")
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        print(f"Element {locator} found. Clicking it now.")
        element.click()

    def wait_locator(self,locator):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

    def onboarding_start(self):
        self.click_start_onboarding_button()
        self.click_lets_complete_button()
        self.upload_button()
        self.next_button()
        self.wait_locator(onboardingLocators.imagUploadingWait)
        self.next_button()
        time.sleep(5)
        self.next_button()
        self.business_logo_upload()
        self.next_button()
        self.description_field()
        self.next_button()
        self.wait_locator(onboardingLocators.businessSummaryWait)
        self.businessSummary_field()
        self.next_button()
        self.primaryIndustry_field()
        self.next_button_1()
        self.next_button()
        self.next_button()
        self.website_url()
        self.linkedIn_Url_Text()
        self.twitter_Url_Text()
        self.facebook_Url_Text()
        self.update_button()
        self.close_button()

        businessBasicToast_alert = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(profileLocators.businessAlert))
        actual_Toast_text = businessBasicToast_alert.text
        expected_Toast_text = "Profile updated successfully"
        assert actual_Toast_text == expected_Toast_text, f"Expected '{expected_Toast_text}', but got '{actual_Toast_text}'"
        time.sleep(2)

        profileCompletion = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(onboardingLocators.profileCompleteText))
        actual_text = profileCompletion.text
        expected_text = "Your profile is 100% complete"
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
