import time

from Utils.profile_locators import profileLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.userprofile_data import UserprofileData


class Userprofile:
    def __init__(self, driver):
        self.driver = driver
    def view_your_profile(self):

        viewProfileButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.viewProfile))
        viewProfileButton.click()
    def click_on_edit(self):
        editButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.editButton))
        editButton.click()
    def edit_profile_info(self):
        tagLine = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.tagLine))
        tagLine.clear()
        tagLine.send_keys(UserprofileData.tagLine)
        aboutME = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.aboutMe))
        aboutME.clear()
        aboutME.send_keys(UserprofileData.aboutMe)
        phoneNumber = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.phoneNumber))
        phoneNumber.clear()
        phoneNumber.send_keys(UserprofileData.phoneNumber)
        websiteUrl = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.webSiteInput))
        websiteUrl.clear()
        websiteUrl.send_keys(UserprofileData.website)
        linkedinUrl = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.linkedinInput))
        linkedinUrl.clear()
        linkedinUrl.send_keys("https://www.linkedin.com/in/asadhafeez15/")
        facebookUrl = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.facebookInput))
        facebookUrl.clear()
        facebookUrl.send_keys("https://www.linkedin.com/in/asadhafeez15/")
        twitterUrl = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.twitterInput))
        twitterUrl.clear()
        twitterUrl.send_keys("https://www.linkedin.com/in/asadhafeez15/")
        instagramUrl = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.instagramInput))
        instagramUrl.clear()
        instagramUrl.send_keys("https://www.linkedin.com/in/asadhafeez15/")
        snapchatUrl = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.snapchatInput))
        snapchatUrl.clear()
        snapchatUrl.send_keys("https://www.linkedin.com/in/asadhafeez15/")
        saveButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.saveBtn))
        saveButton.click()
    def preview_profile(self):
        previewButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.previewButton))
        previewButton.click()
    def exit_preview(self):
        exitPreview = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.exitPreview))
        exitPreview.click()
    def user_profile(self):
        self.preview_profile()
        self.click_on_edit()
        time.sleep(5)
        self.edit_profile_info()
        self.preview_profile()
        time.sleep(10)
        self.exit_preview()












