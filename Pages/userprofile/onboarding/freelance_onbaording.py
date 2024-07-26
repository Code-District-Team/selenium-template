import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.userprofile.onboarding.onboarding_page import OnboardingPage
from Utils.onboardingLocators import onboardingLocators
from Utils.profile_locators import profileLocators


class FreelanceOnboardingPage:
    def __init__(self, driver):
        self.driver = driver

    def snapchatUrl(self):
        snapchatUrl = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.snapchatUrlText))
        snapchatUrl.send_keys("https://www.snapchat.com/add/asad_hafeez?share_id=9zDzsurRCVE&locale=en-GB")

    def instagramUrl(self):
        instagramUrl = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.instgramUrlText))
        instagramUrl.send_keys("https://www.instagram.com/asadhafeez_/")

    def projecttitle(self):
        tileText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.titleText))
        tileText.send_keys("Eat and sleep")

    def description(self):
        descriptionText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.projectDescription))
        descriptionText.send_keys("This is my test project")

    def projecturl(self):
        projectURL = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboardingLocators.projectUrl))
        projectURL.send_keys("https://development.d2vtpkgl21lrum.amplifyapp.com/")

    def businessdescription(self):
        businessOverviewDescription = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.descriptionInputText))
        businessOverviewDescription.send_keys("Lets do it")
        time.sleep(3)

    def updatebutton(self):
        updateButton = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboardingLocators.updateButtonFreelance))
        updateButton.click()

    def freelanceonboarding(self, driver_setup):
        onboarding_page_instance = OnboardingPage(driver_setup)
        onboarding_page_instance.click_start_onboarding_button()
        time.sleep(2)
        onboarding_page_instance.click_lets_complete_button()
        onboarding_page_instance.upload_button()
        time.sleep(2)
        onboarding_page_instance.tagline()
        onboarding_page_instance.website_url()
        onboarding_page_instance.linkedIn_Url_Text()
        onboarding_page_instance.twitter_Url_Text()
        onboarding_page_instance.facebook_Url_Text()
        self.instagramUrl()
        self.snapchatUrl()
        onboarding_page_instance.next_button_1()
        time.sleep(1)
        onboarding_page_instance.next_button()
        time.sleep(1)
        onboarding_page_instance.next_button()
        time.sleep(1)
        onboarding_page_instance.business_logo_upload()
        self.projecttitle()
        time.sleep(1)
        self.description()
        time.sleep(1)
        self.projecturl()
        onboarding_page_instance.next_button_1()
        time.sleep(1)
        self.businessdescription()
        self.updatebutton()
        time.sleep(1)
        onboarding_page_instance.close_button()

        freelanceToast_alert = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(profileLocators.businessAlert))
        actual_loginToast_text = freelanceToast_alert.text
        expected_loginToast_text = "Profile updated successfully"
        assert actual_loginToast_text == expected_loginToast_text, f"Expected '{expected_loginToast_text}', but got '{actual_loginToast_text}'"

        profileCompletion = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(onboardingLocators.profileCompleteText))
        actual_text = profileCompletion.text
        expected_text = "Your profile is 100% complete"
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
