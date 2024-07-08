import time


from Utils.profile_locators import profileLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utils.mynetwork_locators import mynetworkLocators
from Pages.MyNetwork.signup_pytest_function import MyNetwork


class NetworkPage:
    def __init__(self, driver):
        self.driver = driver
    def follow_send_business_card(self):
        followUser = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.followButton))
        followUser.click()
        time.sleep(2)
    def send_business_card(self):
        sendBusinessCard = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.sendBusinessCard))
        sendBusinessCard.click()
        time.sleep(5)
        sendRequest = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.sendRequest))
        sendRequest.click()
    def navigate_to_mynetwork(self):
        networkTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.networkTab))
        networkTab.click()
    def navigate_to_following_tab(self):
        followingTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.followingTab))
        followingTab.click()
    def verify_following_tab(self):
        getUserBFollowing = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.userBFollowing))
        userB = getUserBFollowing.text
        if userB == MyNetwork.name2:
            print("User A is following user B")
        else:
            print("User B is not following user A")
    def navigate_to_business_card_tab(self):
        businessCardTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.businessCardTab))
        businessCardTab.click()
    def navigate_to_sent_business_card_tab(self):
        sentBusinessCardTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.sentBusinessCardTab))
        sentBusinessCardTab.click()
    def verify_sent_business_card_tab(self):
        getUserBBusinessCard = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.userABusinessCard))
        userB = getUserBBusinessCard.text
        if userB == MyNetwork.name2:
            print("User A has sent business card to user B")
        else:
            print("User B has not sent business card to user A")
    def sign_out(self):
        profileAvtar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.profileAvtar))
        profileAvtar.click()
        time.sleep(5)
        sign_outButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.sign_outButton))
        sign_outButton.click()
    def navigate_to_login_page(self):
        loginButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.loginButton))
        loginButton.click()
    def accept_business_card(self):
        acceptButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.acceptButton))
        acceptButton.click()
        time.sleep(10)
        notificationButton = WebDriverWait(self.driver, 30).until( EC.element_to_be_clickable(profileLocators.notificationButton))
        notificationButton.click()
    def verify_contacts(self):
        getUserA = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.userBFollowing))
        userA = getUserA.text
        if userA == MyNetwork.name1:
            print("User A has the contact of user B")
        else:
            print("User A has not the contact of user B")
    def navigate_to_followers_tab(self):
        followersTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.followersTab))
        followersTab.click()
    def verify_followers_tab(self):
        getUserAFollowers = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.userBFollowing))
        userA = getUserAFollowers.text
        if userA == MyNetwork.name1:
            print("User A has the follower of user B")
        else:
            print("User A has not the follower of user B")
    def unfollow_User(self):
        unfollowButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.unfollowUser))
        unfollowButton.click()
    def verify_user_unfollowed(self):
        findFollowing = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.findFollowingButton))
        findFollowing = findFollowing.text
        if findFollowing != MyNetwork.name1:
            print("User B has unfollowed user A")
        else:
            print("User B has not unfollowed user A")
    def block_user_request(self):
        viewBusinessCardRequest = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.viewBusinessCardRequest))
        viewBusinessCardRequest.click()
        blockButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.blockUser))
        blockButton.click()
        time.sleep(3)
        notificationButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.notificationButton))
        notificationButton.click()
    def navigate_to_block_tab(self):
        contactsTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.blockTab))
        contactsTab.click()

    def verify_block_tab(self):
        getUserABlock = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.userBFollowing))
        userA = getUserABlock.text
        if userA == MyNetwork.name1:
            print("User b has blocked user A")
        else:
            print("User b has not blocked user A")
    def unblock_user(self):
        unblockButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.unblockUser))
        unblockButton.click()
    def verify_user_unblocked(self):
        displayedMessage = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.displayedMessage))
        displayedMessage = displayedMessage.text
        if displayedMessage != MyNetwork.name1:
            print("User B has unblocked user A")
        else:
            print("User B has not unblocked user A")


    def network_Tab_for_UserA(self):
        self.navigate_to_mynetwork()
        self.navigate_to_following_tab()
        self.verify_following_tab()
        time.sleep(3)
        self.navigate_to_business_card_tab()
        self.navigate_to_sent_business_card_tab()
        self.verify_sent_business_card_tab()
        self.sign_out()
        time.sleep(3)
        self.navigate_to_login_page()
    def network_Tab_for_UserB(self):
        self.accept_business_card()
        time.sleep(2)
        self.navigate_to_mynetwork()
        time.sleep(2)
        self.verify_contacts()
        self.navigate_to_followers_tab()
        self.verify_followers_tab()
        self.unfollow_User()
        time.sleep(2)
        self.navigate_to_following_tab()
        time.sleep(2)
        self.verify_user_unfollowed()
        time.sleep(2)
        self.navigate_to_followers_tab()
        time.sleep(5)
    def block_business_card_request(self):
        self.block_user_request()
        self.navigate_to_mynetwork()
        self.navigate_to_block_tab()
        self.verify_block_tab()
        self.unblock_user()
        self.verify_user_unblocked()


