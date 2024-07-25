import time
from faker import Faker


from selenium.webdriver import Keys

from Utils.teamLocator import teamLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
faker = Faker()
class  teamPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_team_page(self):
        verifyBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.verifyAccountBtn))
        verifyBtn.click()
        businessTabBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.businessTabBtn))
        businessTabBtn.click()
        teamTab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.teamTab))
        teamTab.click()

    def invite_administrator(self):
        time.sleep(3)
        inviteAdminBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.inviteAdminBtn))
        inviteAdminBtn.click()


    def invite_internal_members(self):
        searchBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.searchBtn))
        searchBtn.click()
        searchBtn.send_keys("david")
        checkBox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.checkBox))
        checkBox.click()

    def invite(self):
        nextBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.nextBtn))
        nextBtn.click()
        inviteBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.inviteBtn))
        inviteBtn.click()

    def invite_external_users(self):
        inviteByEmail = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.inviteByEmail))
        inviteByEmail.click()
        enterEmail = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.enterEmail))
        enterEmail.click()
        enterEmail.send_keys(faker.email())
        submitBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.submitBtn))
        submitBtn.click()
        time.sleep(2)
        enterEmail.send_keys(faker.email())
        submitBtn.click()
        time.sleep(1)
        enterEmail.send_keys(faker.email())
        submitBtn.click()
        time.sleep(1)
    def success_message(self):
        successMessage = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.successMessage))
        message = successMessage.text
        print(message)
        expectedMessage = "3 Invitation(s) sent successfully."
        assert message == expectedMessage

    def delete_member(self):
        moreDropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.moreDropdown))
        moreDropdown.click()
        deleteBtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.deleteBtn))
        deleteBtn.click()
        deleteSuccessMessage = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(teamLocator.deleteSuccessMessage)).text
        text = "Invitation has been deleted."

        assert deleteSuccessMessage == text


    def team_internal_members_invite(self):
        self.navigate_to_team_page()
        self.invite_administrator()
        self.invite_internal_members()

    def team_external_members(self):
        self.navigate_to_team_page()
        self.invite_administrator()
        self.invite_external_users()
        self.invite()
        self.success_message()
        self.delete_member()