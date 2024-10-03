from faker import Faker
from selenium.webdriver import Keys

# from Utils.teamLocator import teamLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.by import By


faker = Faker()





class teamLocator:
    profileAvtar = (By.ID, "profileAvatar")
    accountSettings = (By.XPATH, "//a[normalize-space()='Account Settings']")
    businessTabBtn = (By.XPATH, "//button[normalize-space()='Business']")
    teamTab = (By.XPATH, "(//button[normalize-space()='Team'])[1]")
    inviteAdminBtn = (By.XPATH, "(//button[normalize-space()='Invite Administrators'])[1]")
    searchBtn = (By.XPATH, "(//input[@placeholder='Name, email, etc...'])[1]")
    checkBox = (By.XPATH, "//li[starts-with(@class, 'MuiListItem')][1]//span[starts-with(@class, 'MuiButtonBase')]//input")
    nextBtn = (By.XPATH, "(//button[normalize-space()='Next'])[1]")
    inviteBtn = (By.XPATH, "(//button[normalize-space()='Invite'])[1]")
    inviteByEmail = (By.XPATH, "(//button[normalize-space()='Invite By Email'])[1]")
    enterEmail = (By.XPATH, "(//input[@placeholder='Enter Your Email'])[1]")
    submitBtn = (By.XPATH, "//button[@type = 'submit']")
    successMessage = (By.XPATH, "(//div[@role='status'])[1]")
    moreDropdown = (By.XPATH, "(//button[@type='button'])[18]")
    deleteBtn = (By.XPATH, "(//li[normalize-space()='Delete'])[1]")
    deleteSuccessMessage = (By.XPATH, "(//div[@role='status'])[1]")
    nextBtn_ = (By.XPATH, "//button[@id='btn-next']")
    nextBtnInvite = (By.XPATH, "//button[@id='btn-invite']")


class teamPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_team_page(self):
        profileAvatar = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(teamLocator.profileAvtar))
        profileAvatar.click()
        accountSettings = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(teamLocator.accountSettings))
        accountSettings.click()
        businessTab = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(teamLocator.businessTabBtn))
        businessTab.click()
        teamTab = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(teamLocator.teamTab))
        teamTab.click()
    def invite_administrator(self):
        time.sleep(3)
        inviteAdminBtn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.inviteAdminBtn))
        inviteAdminBtn.click()

    def invite_internal_members(self):
        searchBtn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.searchBtn))
        searchBtn.click()

        searchBtn.send_keys("david")
        time.sleep(5)
        addmember_ = self.driver.find_element(*teamLocator.checkBox)
        addmember_.send_keys(Keys.SPACE)
        searchBtn.clear()

        searchBtn.send_keys("john")
        time.sleep(5)
        addmember_ = self.driver.find_element(*teamLocator.checkBox)
        addmember_.send_keys(Keys.SPACE)
        searchBtn.clear()

        searchBtn.send_keys("smith")
        time.sleep(5)
        addmember_ = self.driver.find_element(*teamLocator.checkBox)
        addmember_.send_keys(Keys.SPACE)

        nextBtn = self.driver.find_element(*teamLocator.nextBtn_)
        nextBtn.click()

        inviteBtn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.nextBtnInvite))
        inviteBtn.click()
        time.sleep(2)

    def invite(self):
        nextBtn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.nextBtn))
        nextBtn.click()
        inviteBtn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.inviteBtn))
        inviteBtn.click()

    def invite_external_users(self):
        inviteByEmail = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.inviteByEmail))
        inviteByEmail.click()
        time.sleep(3)
        enterEmail = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.enterEmail))
        enterEmail.click()
        enterEmail.send_keys(faker.email())
        submitBtn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.submitBtn))
        submitBtn.click()
        time.sleep(2)
        enterEmail.send_keys(faker.email())
        submitBtn.click()
        time.sleep(2)
        enterEmail.send_keys(faker.email())
        submitBtn.click()
        time.sleep(2)

    def success_message(self):
        successMessage = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.successMessage))
        message = successMessage.text
        print(message)
        expectedMessage = "3 Invitation(s) sent successfully."
        assert message == expectedMessage

    def delete_member(self):
        moreDropdown = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.moreDropdown))
        moreDropdown.click()
        deleteBtn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(teamLocator.deleteBtn))
        deleteBtn.click()
        time.sleep(2)
        deleteSuccessMessage = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(teamLocator.deleteSuccessMessage)).text
        print(deleteSuccessMessage)
        text = "Invitation has been deleted."
        time.sleep(5)

        assert deleteSuccessMessage == text

    def team_internal_members_invite(self):
        self.navigate_to_team_page()
        time.sleep(3)
        self.invite_administrator()
        self.invite_internal_members()
        self.success_message()

    def team_external_members(self):
        self.invite_administrator()
        self.invite_external_users()
        self.invite()
        self.success_message()
        self.delete_member()