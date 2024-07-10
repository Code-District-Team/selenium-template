from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils.verify_account_locators import VerifyAccountLocator
from selenium.webdriver.support import expected_conditions as EC

class VerifyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def click_profile_avatar(self):
        profile_click = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.profileAvatar))
        profile_click.click()

    def click_verify_account(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.verifyAccount)).click()

    def click_inviteReviewer(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.inviteReviewer)).click()

    def click_searchBar(self):
       searchBar = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.searchBar)).click()
       searchBar.send_keys("david")

    def check_user_list(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.userList1)).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.userList2)).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.userList3)).click()

    def click_selected_invitee(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.selectedInvitee)).click()



    def verify_account(self):
        self.click_profile_avatar()
        self.verify_account()
        self.click_inviteReviewer()
        self.click_searchBar()
        self.check_user_list()
        self.click_selected_invitee()