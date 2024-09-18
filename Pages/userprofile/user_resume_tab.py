import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.userprofile_data import UserprofileData
from Pages.userprofile.user_profile import Userprofile



class profile_Locators:
    profileAvatar = (By.XPATH, "//div[@id='profileAvatar']//*[name()='svg']")
    viewProfile = (By.XPATH, "//a[normalize-space()='My Profile']")
    saveBtn = (By.XPATH, "(//button[normalize-space()='Save'])")
    resumeTab = (By.XPATH, "(//button[normalize-space()='Resume'])[1]")
    addExperienceButton = (By.XPATH, "//button[normalize-space()='Add Experience']")
    jobTitle = (By.XPATH, "//input[contains(@class, 'MuiInputBase-inputAdornedEnd')]")
    employerInput = (By.XPATH, "(//input[@aria-autocomplete='list'])[2]")
    employerInputOption = (By.XPATH,
                           "(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary mui-1bhfyc0'][normalize-space()='Code District'])[1]")
    startDate = (By.XPATH, "//input[@placeholder='MMMM YYYY']")
    startDateYear = (By.XPATH, "//button[normalize-space()='2019']")
    startDateMonth = (By.XPATH, "//button[normalize-space()='Mar']")

    currentlyCheckbox = (By.XPATH, "//span[normalize-space()='Currently']")
    description = (By.NAME, "jobDescription")
    saveButton = (By.XPATH, "//button[normalize-space()='Save']")
    addEducationButton = (By.XPATH, "//button[normalize-space()='Add Education']")
    fieldOfStudy = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]")
    fieldOfStudyOption = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/ul[1]/li[1]")
    edInstitute = (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/input[1]")
    addEducationButtonPop = (By.XPATH, "(//button[@type='submit'][normalize-space()='Add Education'])[1]")
    addSkillsButton = (By.XPATH, "//button[normalize-space()='Add Skills']")
    enterSkills = (
        By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    skillOption = (By.XPATH, "//li[@role='option' and @aria-selected='false' and @aria-disabled='false' and text()='0-1 drop indicators']")
    addSkill = (By.XPATH,
                "(//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeSmall MuiButton-outlinedSizeSmall MuiButton-colorPrimary MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeSmall MuiButton-outlinedSizeSmall MuiButton-colorPrimary btn-email mui-7jyovo'])[1]")
    doneButton = (By.XPATH, "//button[normalize-space()='Done']")
    addPersonalHonoorsButton = (By.XPATH, "//button[normalize-space(text())='Add Personal Honors and Certifications']")
    honorDate = (By.XPATH, "//input[@placeholder='MMMM YYYY']")
    certificateName = (By.XPATH, "//textarea[@name='certificationName']")
    addWorkPublishButton = (By.XPATH, "//button[normalize-space()='Add works published']")
    workPublishDate = (By.XPATH, "//input[@placeholder='MMMM YYYY']")
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


class User_resume:
    def __init__(self, driver):
        self.driver = driver
    def view_your_profile(self):

        profileAvatar = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.profileAvatar))
        profileAvatar.click()

        viewProfile = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.viewProfile))
        viewProfile.click()

    def navigate_on_resume_tab(self):
        resumeTab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profile_Locators.resumeTab))
        resumeTab.click()

    def add_experience(self):
        addExperience = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(profile_Locators.addExperienceButton))
        addExperience.click()
        self.driver.execute_script("window.scrollBy(0, window.innerHeight/2);")
        jobTitleDropdown = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.jobTitle))
        jobTitleDropdown.click()
        jobTitleDropdown.send_keys("Code Inspector")
        time.sleep(5)
        jobTitleDropdown.send_keys(Keys.ENTER)
        employerInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.employerInput))
        employerInput.click()
        employerInput.send_keys("code distrcit vv5")
        time.sleep(5)
        employerInput.send_keys(Keys.ARROW_UP, Keys.ENTER)
        startDate = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profile_Locators.startDate))
        startDate.click()
        startDateInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.startDateYear))
        startDateInput.click()
        startDateMonth = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.startDateMonth))
        startDateMonth.click()
        currentlyCheckbox = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.currentlyCheckbox))
        currentlyCheckbox.click()
        descriptionInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.description))
        descriptionInput.send_keys("A great place to work")
        addExperienceButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.saveButton))
        addExperienceButton.click()

    def add_education(self):
        fieldOfStudy = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.fieldOfStudy))
        fieldOfStudy.click()
        fieldOfStudyOption = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.fieldOfStudyOption))
        fieldOfStudyOption.click()

    def add_skills(self):
        addSkillButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.addSkillsButton))
        addSkillButton.click()
        enterSkills = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.enterSkills))
        enterSkills.click()
        skillOption = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.skillOption))
        skillOption.click()
        addSkill = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.addSkill))
        addSkill.click()
        doneButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.doneButton))
        doneButton.click()

    def work_published(self):
        addWorkPublish = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.addWorkPublishButton))
        addWorkPublish.click()
        publishDate = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.workPublishDate))
        publishDate.click()
        time.sleep(1)
        publishDateOption = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.startDateYear))
        publishDateOption.click()
        publishDateOptionMonth = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.startDateMonth))
        publishDateOptionMonth.click()
        titleInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.titleField))
        titleInput.send_keys("Afghanistan alternative solutions")
        authorInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.authorField))
        authorInput.send_keys("Naveed Mukhtar")
        urlInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.urlInput))
        urlInput.send_keys("https://pildat.org/wp-content/uploads/2019/04/stateofcivilmilitaryrelationsinpakistan_astudyof5years20132018.pdf?")
        doneButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.doneButton))
        doneButton.click()

    def personal_honors(self):
        add_personalhonors = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profile_Locators.addPersonalHonoorsButton))
        add_personalhonors.click()
        personalHonorDate = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.honorDate))
        personalHonorDate.click()
        yearOption = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.startDateYear))
        yearOption.click()
        monthOption = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.startDateMonth))
        monthOption.click()
        certificateName = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.certificateName))
        certificateName.send_keys(UserprofileData.certificateName)
        doneButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.doneButton))
        doneButton.click()

    def add_reference(self):
        manageProfessionalReference = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.manageReference))
        manageProfessionalReference.click()
        time.sleep(5)

        # Retry mechanism for inviteButton
        for _ in range(3):
            try:
                inviteButton = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(profile_Locators.inviteButton))
                inviteButton.click()
                break
            except StaleElementReferenceException:
                pass

        # Retry mechanism for markMember
        for _ in range(3):
            try:
                markMember = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.markMember))
                markMember.click()
                break
            except StaleElementReferenceException:
                pass

        inviteSelected = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(profile_Locators.inviteSelected))
        inviteSelected.click()

    def test_resume(self, driver):
        navigateToProfile = Userprofile(driver)
        navigateToProfile.view_your_profile()
        time.sleep(5)
        self.navigate_on_resume_tab()
        time.sleep(5)
        self.add_experience()
        time.sleep(5)
        self.add_skills()
        time.sleep(2)
        self.work_published()
        time.sleep(5)
        self.personal_honors()
        time.sleep(5)
        #self.add_reference()
        time.sleep(20)
