from selenium.webdriver.common.by import By
class VerifyAccountLocator:
    profileAvatar = (By.ID, "profileAvatar")
    verifyAccount = (By.ID, "verifyAccount")
    inviteReviewer = (By.ID, "vertical-tab-2")
    searchBar = (By.XPATH, "//input[@placeholder = 'Name, email, etc...']")
    userList1 = (By.XPATH, "(//input[@class ='PrivateSwitchBase-input mui-1m9pwf3'])[1]")
    userList2 = (By.XPATH, "(//input[@class ='PrivateSwitchBase-input mui-1m9pwf3'])[2]")
    userList3 = (By.XPATH, "(//input[@class ='PrivateSwitchBase-input mui-1m9pwf3'])[3]")
    selectedInvitee = (By.ID, "verifyInviteSelected")
