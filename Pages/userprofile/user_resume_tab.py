import time

from Utils.profile_locators import profileLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.userprofile_data import UserprofileData
from Pages.userprofile.user_profile import Userprofile


class User_resume:
    def __init__(self, driver):
        self.driver = driver
    def navigate_on_resume_tab(self):
        resumeTab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.resumeTab))
        resumeTab.click()
    def add_experience(self):
        addExperience = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.addExperienceButton))
        addExperience.click()
        jobTitleDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.jobTitleDropdown))
        jobTitleDropdown.click()
        jobTitleOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.jobTitleOption))
        jobTitleOption.click()
        employerInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.employerInput))
        employerInput.click()
        employerInput.send_keys("cod")
        employerOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.employerInputOption))
        employerOption.click()
        startDate = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.startDate))
        startDate.click()
        startDateInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.startDateOption))
        startDateInput.click()
        currentlyCheckbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.currentlyCheckbox))
        currentlyCheckbox.click()
        descriptionInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.description))
        descriptionInput.send_keys("A great place to work")
        addExperienceButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.addExperienceButtonPopup))
        addExperience.click()
    def add_education(self):
        fieldOfStudy = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.fieldOfStudy))
        fieldOfStudy.click()
        fieldOfStudyOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.fieldOfStudyOption))
        fieldOfStudyOption.click()
    def add_skills(self):
        addSkillButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.addSkillsButton))
        addSkillButton.click()
        enterSkills = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.enterSkills))
        enterSkills.click()
        skillOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.skillOption))
        skillOption.click()
        addSkill = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.addSkill))
        addSkill.click()
        doneButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.doneButton))
        doneButton.click()
    def work_published(self):
        addWorkPublish = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.addWorkPublishButton))
        addWorkPublish.click()
        publishDate = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.workPublishDate))
        publishDate.click()
        titleInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.titleField))
        titleInput.send_keys("Afghanistan alternative solutions")
        authorInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.authorField))
        authorInput.send_keys("Naveed Mukhtar")
        urlInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.urlInput))
        urlInput.send_keys("https://pildat.org/wp-content/uploads/2019/04/stateofcivilmilitaryrelationsinpakistan_astudyof5years20132018.pdf?")
        doneButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.doneButton))
        doneButton.click()
    def personal_honors(self):
        add_personalhonors = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.addPersonalHonoorsButton))
        add_personalhonors.click()
        personalHonorDate = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.honorDate))
        personalHonorDate.click()
        startDateOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.startDateOption))
        startDateOption.click()
        certificateName = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.certificateName))
        certificateName.send_keys(UserprofileData.certificateName)
        doneButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.doneButton))
        doneButton.click()
    def add_reference(self):
        manageProfessionalReference = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.manageReference))
        manageProfessionalReference.click()
        inviteButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.inviteButton))
        inviteButton.click()
        markMember = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.markMember))
        markMember.click()
        inviteSelected = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.inviteSelected))
        inviteSelected.click()
    def test_resume(self, driver):
        navigateToProfile = Userprofile(driver)
        navigateToProfile.view_your_profile()
        self.navigate_on_resume_tab()
        time.sleep(10)
        self.add_experience()
        time.sleep(50)
        self.add_education()
        time.sleep(30)
        self.add_skills()
        time.sleep(20)
        self.work_published()
        time.sleep(20)
        self.personal_honors()
        time.sleep(20)
        self.add_reference()
        time.sleep(30)














