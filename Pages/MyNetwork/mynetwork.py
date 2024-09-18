import time

from Utils.profile_locators import profileLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.MyNetwork.signup_pytest_function import MyNetwork
from selenium.webdriver.common.by import By

class mynetworkLocators:
    networkTab = (By.XPATH, "//span[normalize-space()='My Network']")
    followingTab = (By.ID, "tab-following")
    networkSearchField = (By.ID, "network-search-field")
    userBFollowing = (By.XPATH, "(//h4[@class='MuiTypography-root MuiTypography-h4 profile-name mui-pu29jg'])[1]")
    businessCardTab = (By.ID, "tab-businessCards")
    sentBusinessCardTab = (By.XPATH, "(//button[normalize-space()='Sent'])[1]")
    userABusinessCard = (By.XPATH, "(//h4[@class='MuiTypography-root MuiTypography-h4 profile-name mui-pu29jg'])[1]")
    profileAvtar = (By.XPATH, "//div[@id='profileAvatar']//*[name()='svg']")
    sign_outButton = (By.XPATH, "//li[normalize-space()='Sign out']")
    followersTab = (By.XPATH, "//button[@id='tab-followers']")
    unfollowUser = (By.XPATH, "//li[1]//div[2]//div[1]//button[3]//*[name()='svg']")
    findFollowingButton = (By.XPATH, "//button[normalize-space()='Find User To Follow']")
    viewBusinessCardRequest = (By.XPATH, "(//button[normalize-space()='View Detail'])[1]")
    blockUser = (By.XPATH, "(//button[normalize-space()='Block User'])[1]")
    blockTab = (By.ID, "tab-blocked")
    unblockUser = (By.XPATH, "(//button[normalize-space()='Unblock'])[1]")
    displayedMessage = (By.XPATH, "//h5[normalize-space()='You have not blocked any users']")
    drawer = (By.XPATH, "//button[@aria-label='open drawer']//*[name()='svg']")





class NetworkPage:
    def __init__(self, driver):
        self.driver = driver

    def half_page_scroll(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        half_height = total_height / 2
        self.driver.execute_script(f"window.scrollTo(0, {half_height});")

    def follow_send_business_card(self):
        followUser = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.followButton))
        followUser.click()
        time.sleep(2)

    def send_business_card(self):
        sendBusinessCard = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(profileLocators.sendBusinessCard))
        sendBusinessCard.click()
        time.sleep(5)
        sendMessage_ = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.sendMessage))
        sendMessage_.click()
        sendMessage_.send_keys(" This is a test message!! ")
        sendRequest = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profileLocators.sendRequest))
        sendRequest.click()
        businessAlert_ = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(profileLocators.businessAlert))
        expected_text = businessAlert_.text
        actual_text = "1 Business Requests sent successfully."
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
        print("User A successfully sent the business card request")
        time.sleep(5)

    def navigate_to_mynetwork(self):
        openDrawer = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.drawer))
        openDrawer.click()
        networkTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.networkTab))
        networkTab.click()
        self.half_page_scroll()

    def navigate_to_following_tab(self):
        followingTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.followingTab))
        followingTab.click()

    def verify_following_tab(self):
        getUserBFollowing = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.userBFollowing))
        userB = getUserBFollowing.text
        if userB == MyNetwork.name2:
            print("User A is following user B")
        else:
            print("User B is not following user A")

    def navigate_to_business_card_tab(self):
        businessCardTab = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.businessCardTab))
        businessCardTab.click()
        self.half_page_scroll()

    def navigate_to_sent_business_card_tab(self):
        sentBusinessCardTab = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.sentBusinessCardTab))
        sentBusinessCardTab.click()

    def verify_sent_business_card_tab(self):
        getUserBBusinessCard = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.userABusinessCard))
        userB = getUserBBusinessCard.text
        if userB == MyNetwork.name2:
            print("User A has sent business card to user B")
        else:
            print("User B has not sent business card to user A")

    def sign_out(self):
        profileAvtar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.profileAvtar))
        profileAvtar.click()
        sign_outButton = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.sign_outButton))
        sign_outButton.click()

    def navigate_to_login_page(self):
        loginButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.loginButton))
        loginButton.click()

    def accept_business_card(self):
        acceptButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(profileLocators.acceptButton))
        acceptButton.click()
        # assertion
        businessAlert_ = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(profileLocators.businessAlert))
        expected_text = businessAlert_.text
        actual_text = "Invitation has been Accepted."
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
        print("User B accepts User A's business card request")
        time.sleep(5)
        notificationButton = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(profileLocators.notificationButton))
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
        self.half_page_scroll()

    def verify_followers_tab(self):
        getUserAFollowers = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.userBFollowing))
        userA = getUserAFollowers.text
        if userA == MyNetwork.name1:
            print("User A has the follower of user B")
        else:
            print("User A has not the follower of user B")

    def unfollow_User(self):
        unfollowButton = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.unfollowUser))
        unfollowButton.click()

    def verify_user_unfollowed(self):
        findFollowing = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.findFollowingButton))
        findFollowing = findFollowing.text
        if findFollowing != MyNetwork.name1:
            print("User B has unfollowed user A")
        else:
            print("User B has not unfollowed user A")

    def block_user_request(self):
        viewBusinessCardRequest = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.viewBusinessCardRequest))
        viewBusinessCardRequest.click()
        blockButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.blockUser))
        blockButton.click()
        time.sleep(3)
        notificationButton = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(profileLocators.notificationButton))
        notificationButton.click()

    def navigate_to_block_tab(self):
        contactsTab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.blockTab))
        contactsTab.click()
        self.half_page_scroll()

    def verify_block_tab(self):
        getUserABlock = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.userBFollowing))
        userA = getUserABlock.text
        if userA == MyNetwork.name1:
            print("User b has blocked user A")
        else:
            print("User b has not blocked user A")

    def unblock_user(self):
        unblockButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(mynetworkLocators.unblockUser))
        unblockButton.click()

    def verify_user_unblocked(self):
        displayedMessage = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(mynetworkLocators.displayedMessage))
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
        time.sleep(2)

    def block_business_card_request(self):
        self.block_user_request()
        self.navigate_to_mynetwork()
        self.navigate_to_block_tab()
        self.verify_block_tab()
        self.unblock_user()
        self.verify_user_unblocked()
