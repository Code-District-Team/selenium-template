import time
import os
import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.userprofile_data import UserprofileData


class profile_Locators:
    profileAvatar = (By.XPATH, "//div[@id='profileAvatar']//*[name()='svg']")
    viewProfile = (By.XPATH, "//a[normalize-space()='My Profile']")
    editButton = (By.XPATH, "//button[normalize-space()='Edit']")
    previewButton = (By.XPATH, "//button[normalize-space()='Preview']")
    tagLine = (By.NAME, "tagline")
    aboutMe = (By.NAME, "aboutMe")
    phoneNumber = (By.XPATH, "//input[@placeholder='1 (702) 123-4567']")
    webSiteInput = (By.NAME, "websiteUrl")
    facebookInput = (By.NAME, "facebookUrl")
    twitterInput = (By.NAME, "twitterUrl")
    instagramInput = (By.NAME, "instagramUrl")
    snapchatInput = (By.NAME, "snapChatUrl")
    linkedinInput = (By.NAME, "linkedInUrl")
    saveBtn = (By.XPATH, "(//button[normalize-space()='Save'])")
    resumeTab = (By.XPATH, "(//button[normalize-space()='Resume'])[1]")
    addExperienceButton = (By.XPATH, "//button[normalize-space()='Add Experience']")
    jobTitleDropdown = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]")
    jobTitleOption = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/ul[1]/li[1]")
    employerInput = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/input[1]")
    employerInputOption = (By.XPATH,
                           "(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary mui-1bhfyc0'][normalize-space()='Code District'])[1]")
    startDate = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[4]/div[1]/div[1]/input[1]")
    startDateOption = (By.XPATH, "//button[normalize-space()='1']")
    currentlyCheckbox = (By.XPATH, "//span[normalize-space()='Currently']")
    description = (By.NAME, "jobDescription")
    addExperienceButtonPopup = (By.XPATH, "//button[@type='submit'][normalize-space()='Add Experience']")
    addEducationButton = (By.XPATH, "//button[normalize-space()='Add Education']")
    fieldOfStudy = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]")
    fieldOfStudyOption = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/ul[1]/li[1]")
    edInstitute = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/input[1]")
    addEducationButtonPop = (By.XPATH, "(//button[@type='submit'][normalize-space()='Add Education'])[1]")
    addSkillsButton = (By.XPATH, "//button[normalize-space()='Add Skills']")
    enterSkills = (
    By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    skillOption = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/ul[1]/li[1]")
    addSkill = (By.XPATH,
                "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeSmall MuiButton-outlinedSizeSmall MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeSmall MuiButton-outlinedSizeSmall btn-email mui-7jyovo']//*[name()='svg']")
    doneButton = (By.XPATH, "//button[normalize-space()='Done']")
    addPersonalHonoorsButton = (By.XPATH, "//button[normalize-space()='Add personal honors and certifications']")
    honorDate = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
    certificateName = (By.XPATH, "//input[@name='certificationName']")
    addWorkPublishButton = (By.XPATH, "//button[normalize-space()='Add works published']")
    workPublishDate = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
    certificateField = (By.NAME, "certificationName")
    workPublishDateOption = (By.XPATH, "//button[normalize-space()='2']")
    titleField = (By.NAME, "title")
    authorField = (By.NAME, "authors")
    exitPreview = (By.XPATH, "//button[normalize-space()='Exit Preview']")
    urlInput = (By.NAME, "url")
    manageReference = (By.XPATH, "//button[normalize-space()='Manage Professional Preferences']")
    inviteButton = (By.XPATH, "//button[normalize-space()='Invite new']")
    markMember = (By.XPATH, '//*[@id="mui-p-7358-P-yoogoInvite"]/ul/div/div/li[1]/div[1]/span/input')
    inviteSelected = (By.XPATH, "//button[normalize-space()='Invite selected']")
    followButton = (By.XPATH, "//a[normalize-space()='Follow']")
    unFollow = (By.XPATH, "//a[normalize-space()='Following']")
    sendBusinessCard = (By.ID, "btn-send-business")
    sendRequest = (By.XPATH, "(//button[normalize-space()='Send Request'])[1]")
    editProfileImage = (By.XPATH,
                        "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault list-avatar-badge mui-vkkhjl']")
    addImage = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 text-primary mui-1w6h4uc']")
    addCoverPhoto = (By.XPATH, "//button[normalize-space()='Change Cover Photo']")
    changeCoverPhoto = (By.ID, "obdBtnChangePhoto")
    loginButton = (By.XPATH, "//a[normalize-space()='Log In']")
    notificationButton = (By.XPATH, "(//div[@class='MuiBackdrop-root MuiModal-backdrop mui-919eu4'])[1]")
    acceptButton = (By.XPATH, "(//button[normalize-space()='Accept'])[1]")
    sendMessage = (By.XPATH, "//textarea[starts-with(@id,':r')]")
    businessAlert = (By.XPATH, "//div[@role='status']")
    loginText = (By.XPATH, "//a[contains(text(),'Log in')]")
    updateBtn = (By.XPATH, "//button[normalize-space()='Update']")


class Userprofile:
    def __init__(self, driver):
        self.driver = driver
    def view_your_profile(self):

        profileAvatar = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.profileAvatar))
        profileAvatar.click()

        viewProfile = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.viewProfile))
        viewProfile.click()

    def wait_and_click(self, locator, timeout=50):

            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()

    def uploadProfileImage(self):
        editProfileImage = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.editProfileImage))
        editProfileImage.click()
        self.wait_and_click(profile_Locators.addImage)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "profile.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(3)
        saveBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profile_Locators.saveBtn))
        saveBtn.click()

    def uploadcoverphoto(self):
        changeCoverPhoto = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profile_Locators.addCoverPhoto))
        changeCoverPhoto.click()
        self.wait_and_click(profile_Locators.changeCoverPhoto)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "background.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(3)
        saveBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profile_Locators.saveBtn))
        saveBtn.click()
        time.sleep(3)


    def click_on_edit(self):
        editButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.editButton))
        editButton.click()
    def edit_profile_info(self):
        tagLine = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.tagLine))
        time.sleep(1)
        tagLine.send_keys(Keys.CONTROL, 'a')  # Select all text
        tagLine.send_keys(Keys.DELETE)
        time.sleep(1)
        tagLine.send_keys(UserprofileData.tagLine)
        aboutME = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.aboutMe))
        aboutME.send_keys(Keys.CONTROL, 'a')
        aboutME.send_keys(Keys.DELETE)
        time.sleep(1)
        aboutME.send_keys(UserprofileData.aboutMe)
        phoneNumber = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.phoneNumber))
        phoneNumber.send_keys(Keys.CONTROL, 'a')
        phoneNumber.send_keys(Keys.DELETE)
        time.sleep(1)
        phoneNumber.send_keys(UserprofileData.phoneNumber)
        websiteUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.webSiteInput))
        websiteUrl.send_keys(Keys.CONTROL, 'a')
        websiteUrl.send_keys(Keys.DELETE)
        time.sleep(1)
        websiteUrl.send_keys(UserprofileData.website)
        linkedinUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.linkedinInput))
        linkedinUrl.send_keys(Keys.CONTROL, 'a')
        linkedinUrl.send_keys(Keys.DELETE)
        time.sleep(1)
        linkedinUrl.send_keys("https://www.linkedin.com/in/asadhafeez15")
        facebookUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.facebookInput))
        facebookUrl.send_keys(Keys.CONTROL, 'a')
        facebookUrl.send_keys(Keys.DELETE)
        time.sleep(1)
        facebookUrl.send_keys("https://www.facebook.com/asad.hafeez.942")
        twitterUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.twitterInput))
        twitterUrl.send_keys(Keys.CONTROL, 'a')
        twitterUrl.send_keys(Keys.DELETE)
        time.sleep(1)
        twitterUrl.send_keys("https://twitter.com/AhmadWaleed")
        instagramUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.instagramInput))
        instagramUrl.send_keys(Keys.CONTROL, 'a')
        instagramUrl.send_keys(Keys.DELETE)
        time.sleep(1)
        instagramUrl.send_keys("https://www.instagram.com/asadhafeez_")
        snapchatUrl = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.snapchatInput))
        snapchatUrl.send_keys(Keys.CONTROL, 'a')
        snapchatUrl.send_keys(Keys.DELETE)
        time.sleep(1)
        snapchatUrl.send_keys("https://www.snapchat.com/add/asad_hafeez?share_id=9zDzsurRCVE&locale=en-GB")
        updateButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.updateBtn))
        updateButton.click()
    def preview_profile(self):
        previewButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.previewButton))
        previewButton.click()
    def exit_preview(self):
        exitPreview = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.exitPreview))
        exitPreview.click()
    def user_profile(self):
        self.view_your_profile()
        time.sleep(2)
        self.uploadProfileImage()
        time.sleep(5)
        self.uploadcoverphoto()
        time.sleep(9)
        self.click_on_edit()
        time.sleep(2)
        self.edit_profile_info()
        time.sleep(5)
        self.preview_profile()
        time.sleep(2)
        self.exit_preview()













