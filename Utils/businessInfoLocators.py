from selenium.webdriver.common.by import By
class businessInfoLocators:
    businessTab = (By.XPATH, "//button[normalize-space()='Business']")
    changeBusinessName = (By.XPATH, "(//button[@type='button'][normalize-space()='Change'])[1]")
    companyNameInput = (By.XPATH, "//label[text()='Company Name']/following-sibling::div//input")
    companyNameSave = (By.XPATH, "(//button[contains(@type,'button')][normalize-space()='Save'])[1]")
    primaryIndustryBrowse = (By.XPATH, "(//button[@id='btn-browse'])[1]")
    revenueInput = (By.XPATH, "//label[text()='Revenue (in thousands USD)']/following-sibling::div//input[@type='number']")
    saveRevenue = (By.XPATH, "//div[contains(@class,'yg-content-wrapper MuiBox-root mui-0')]//div[4]//div[1]//div[1]//div[2]//div[2]//button[1]")
    numberOfEmployee = (By.XPATH, "//body[1]/div[4]/div[3]/div[1]/div[3]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    businessContact = (By.XPATH, "//input[@name='businessContact']")
    businessContactFax = (By.XPATH, "//input[@name='businessFax']")
    changeBusinessContact = (By.XPATH, "//div[@class='MuiPaper-root MuiPaper-outlined MuiPaper-rounded MuiCard-root account-card !relative mui-r4co1p']//button[@id='change-info']")
    businessEmail = (By.NAME, "businessEmail")
    changeLocation = (By.XPATH, "(//button[@id='change-info'])[7]")
    countryDropdown = (By.XPATH, "//input[@autocomplete='select-country']")
    stateDropdown = (By.XPATH, "//div[@id='mui-component-select-province']")
    stateDropdownOption = (By.XPATH, "//li[normalize-space()='Berat (AL-01)']")
    cityInput = (By.ID, "city")
    zipCode = (By.ID, "zip-code")
    streetAddress = (By.ID, "street-address")
    saveLocation = (By.XPATH, "//button[@type='submit']")
    skipAccountVerification = (By.ID, "verifyBtnSkip")
    avatar = (By.XPATH, "//div[@id='profileAvatar']")
    accountsettingbtn = (By.XPATH, "//a[text()='Account Settings']")






