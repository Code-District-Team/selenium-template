from selenium.webdriver.common.by import By


class buyerIntentLocators:
    profileAvtar = (By.ID, "profileAvatar")
    buyerProfile = (By.XPATH, "//li[normalize-space()='My buyer profile']")
    browserButton = (By.ID, "btn-browse")
    serviceTypeParentOption = (By.XPATH, "//h6[normalize-space()='Information (2)']")
    serviceTypeChildOption = (By.XPATH, "//p[normalize-space()='Data Processing, Hosting, and Related Services (1)']")
    serviceTypeChildOption_1 = (By.XPATH, "(//span[@class='MuiTypography-root MuiTypography-body1 MuiFormControlLabel-label mui-1w6h4uc'])[1]")
    doneButton = (By.ID, "areaOfInterestBtnDone")
    interestLevelInput = (By.ID, "mui-component-select-interestLevel")
    interestLevelOption = (By.XPATH, "//li[normalize-space()='Planning budgeting']")
    submitButton = (By.XPATH, "//button[@type='submit']")
    productTab = (By.XPATH, "//button[normalize-space()='Products']")
    productTabParentOption = (By.XPATH, "//h6[normalize-space()='Retail Trade (13)']")
    productTabChildOption = (By.XPATH, "(//p[normalize-space()='Other Motor Vehicle (3)'])[1]")
    productTabChildOption1 =(By.XPATH, "//span[normalize-space()='Recreational Vehicle']")
    deleteIcon = (By.XPATH, "//div[@class='table-actions MuiBox-root mui-0']//button[@type='button']//*[name()='svg']")
    deleteConfirmation = (By.XPATH, "//button[normalize-space()='Delete']")





    
    




