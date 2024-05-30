import time

from Utils.profile_locators import profileLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class userprofile:
    def __init__(self, driver):
        self.driver = driver

    def follow_user(self):
        followButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profileLocators.followButton))
        followButton.click()
    def unfollow_user(self):
        unfollowButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profileLocators.unFollow))
        unfollowButton.click()
    def sendBusinessCardRequest(self):
        sendBusinessCard = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profileLocators.sendBusinessCard))
        sendBusinessCard.click()
        sendRequest = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(profileLocators.sendRequest))
        sendRequest.click()
    def test_userprofile(self):
        self.follow_user()
        time.sleep(10)
        self.unfollow_user()
        time.sleep(10)
        self.sendBusinessCardRequest()
        time.sleep(10)
