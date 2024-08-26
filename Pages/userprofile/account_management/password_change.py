import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

faker = Faker()

from selenium.webdriver.common.by import By


class profileLocators:
    viewProfile = (By.ID, "btnViewYourProfile")
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
    saveBtn = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
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
                        "/html[1]/body[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/*[name()='svg'][1]/*[name()='path'][1]")
    addImage = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 text-primary mui-1w6h4uc']")
    addCoverPhoto = (By.XPATH, "//button[normalize-space()='Change Cover Photo']")
    changeCoverPhoto = (By.ID, "obdBtnChangePhoto")
    loginButton = (By.XPATH, "//a[normalize-space()='Log In']")
    notificationButton = (By.XPATH, "(//div[@class='MuiBackdrop-root MuiModal-backdrop mui-919eu4'])[1]")
    acceptButton = (By.XPATH, "(//button[normalize-space()='Accept'])[1]")
    sendMessage = (By.XPATH, "//textarea[starts-with(@id,':r')]")
    businessAlert = (By.XPATH, "//div[@role='status']")
    loginText = (By.XPATH, "//a[contains(text(),'Log in')]")
class email_password_locators:
    skip_onboarding = (By.ID, "verifyBtnSkip")
    emai_tab = (By.XPATH, "(//button[normalize-space()='Email & Password'])[1]")
    change_email_button = (By.ID, "change-email")
    new_email_field = (By.ID, "new-email")
    retype_email_field = (By.ID, "repeat-new-email")
    cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    change_password_button = (By.ID, "btnChangePassword")
    old_password_field = (By.NAME, "oldPassword")
    new_password_field = (By.NAME, "newPassword")
    repeat_password_filed = (By.NAME, "repeatNewPassword")
    save_button = (By.ID, "btn-save")




class password_change:
    newPassword = None

    def __init__(self, driver):
        self.driver = driver

    def change_password_button(self):
        change_password_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.change_password_button))
        change_password_button.click()

    def enter_old_password(self, password):
        old_password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.old_password_field))
        old_password_field.click()
        old_password_field.send_keys(password)
        print("Old Password: " + password)

    def enter_new_password(self):
        new_password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.new_password_field))
        new_password_field.click()
        newPassword = faker.password()
        new_password_field.send_keys(newPassword)
        print("New Password: " + newPassword)
        return newPassword

    def repeat_new_password(self, newPass):
        repeat_password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.repeat_password_filed))
        repeat_password_field.click()
        repeat_password_field.send_keys(newPass)
        print("ReEnter Password: " + newPass)

    def save_password(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(email_password_locators.save_button))
        save_button.click()
        time.sleep(3)

    def change_password(self, password):
        self.change_password_button()
        self.enter_old_password(password)
        newPass = self.enter_new_password()
        self.repeat_new_password(newPass)
        self.save_password()

        PasswordChangeToast_alert = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(profileLocators.businessAlert))
        actual_PasswordChangeToast_text = PasswordChangeToast_alert .text
        expected_PasswordChangeToast_text = "Password updated successfully"
        assert actual_PasswordChangeToast_text == expected_PasswordChangeToast_text, f"Expected '{expected_PasswordChangeToast_text}', but got '{actual_PasswordChangeToast_text }'"

        return newPass