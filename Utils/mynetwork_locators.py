from selenium.webdriver.common.by import By

class mynetworkLocators:
    networkTab = (By.XPATH, '(//li[@role=\'menuitem\'])[3]')
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


