import time
import os
import pyautogui
from selenium.webdriver import Keys

from Utils.profile_locators import profileLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.userprofile_data import UserprofileData


class Userprofile:
    def __init__(self, driver):
        self.driver = driver
    def view_your_profile(self):

        viewProfileButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.viewProfile))
        viewProfileButton.click()

    def wait_and_click(self, locator, timeout=50):

            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()

    def uploadProfileImage(self):
        editProfileImage = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.editProfileImage))
        editProfileImage.click()
        self.wait_and_click(profileLocators.addImage)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "profile.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(3)
        saveBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profileLocators.saveBtn))
        saveBtn.click()

    def uploadcoverphoto(self):
        changeCoverPhoto = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profileLocators.addCoverPhoto))
        changeCoverPhoto.click()
        self.wait_and_click(profileLocators.changeCoverPhoto)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "background.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(3)
        saveBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profileLocators.saveBtn))
        saveBtn.click()


    def click_on_edit(self):
        editButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.editButton))
        editButton.click()
    def edit_profile_info(self):
        tagLine = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.tagLine))
        time.sleep(2)
        tagLine.send_keys(Keys.CONTROL, 'a')  # Select all text
        tagLine.send_keys(Keys.DELETE)
        time.sleep(2)
        tagLine.send_keys(UserprofileData.tagLine)
        aboutME = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.aboutMe))
        aboutME.send_keys(Keys.CONTROL, 'a')
        aboutME.send_keys(Keys.DELETE)
        time.sleep(5)
        aboutME.send_keys(UserprofileData.aboutMe)
        phoneNumber = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.phoneNumber))
        phoneNumber.send_keys(Keys.CONTROL, 'a')
        phoneNumber.send_keys(Keys.DELETE)
        time.sleep(2)
        phoneNumber.send_keys(UserprofileData.phoneNumber)
        websiteUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.webSiteInput))
        websiteUrl.send_keys(Keys.CONTROL, 'a')
        websiteUrl.send_keys(Keys.DELETE)
        time.sleep(2)
        websiteUrl.send_keys(UserprofileData.website)
        linkedinUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.linkedinInput))
        linkedinUrl.send_keys(Keys.CONTROL, 'a')
        linkedinUrl.send_keys(Keys.DELETE)
        time.sleep(2)
        linkedinUrl.send_keys("https://www.linkedin.com/in/asadhafeez15")
        facebookUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.facebookInput))
        facebookUrl.send_keys(Keys.CONTROL, 'a')
        facebookUrl.send_keys(Keys.DELETE)
        time.sleep(2)
        facebookUrl.send_keys("https://www.facebook.com/asad.hafeez.942")
        twitterUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.twitterInput))
        twitterUrl.send_keys(Keys.CONTROL, 'a')
        twitterUrl.send_keys(Keys.DELETE)
        time.sleep(2)
        twitterUrl.send_keys("https://twitter.com/AhmadWaleed")
        instagramUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.instagramInput))
        instagramUrl.send_keys(Keys.CONTROL, 'a')
        instagramUrl.send_keys(Keys.DELETE)
        time.sleep(2)
        instagramUrl.send_keys("https://www.instagram.com/asadhafeez_")
        snapchatUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.snapchatInput))
        snapchatUrl.send_keys(Keys.CONTROL, 'a')
        snapchatUrl.send_keys(Keys.DELETE)
        time.sleep(2)
        snapchatUrl.send_keys("https://www.snapchat.com/add/asad_hafeez?share_id=9zDzsurRCVE&locale=en-GB")
        saveButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.saveBtn))
        saveButton.click()
    def preview_profile(self):
        previewButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.previewButton))
        previewButton.click()
    def exit_preview(self):
        exitPreview = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profileLocators.exitPreview))
        exitPreview.click()
    def user_profile(self):
        self.view_your_profile()
        time.sleep(5)
        self.uploadProfileImage()
        time.sleep(20)
        self.uploadcoverphoto()
        time.sleep(30)
        self.click_on_edit()
        time.sleep(5)
        self.edit_profile_info()
        time.sleep(10)
        self.preview_profile()
        time.sleep(10)
        self.exit_preview()
        time.sleep(10)












