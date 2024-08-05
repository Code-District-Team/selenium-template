from selenium.webdriver.common.by import By

class teamLocator:
    verifyAccountBtn = (
    By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium mui-vubbuv'])[22]")
    dontShow = (By.XPATH, "//input[@type='checkbox']")
    businessTabBtn = (By.XPATH, "(//button[normalize-space()='Business'])[1]")
    teamTab = (By.XPATH, "(//button[normalize-space()='Team'])[1]")
    inviteAdminBtn = (By.XPATH, "(//button[normalize-space()='Invite Administrators'])[1]")
    searchBtn = (By.XPATH, "(//input[@placeholder='Name, email, etc...'])[1]")
    checkBox = (
    By.XPATH, "//li[starts-with(@class, 'MuiListItem')][1]//span[starts-with(@class, 'MuiButtonBase')]//input")
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