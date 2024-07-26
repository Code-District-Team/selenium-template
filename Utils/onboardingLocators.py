from selenium.webdriver.common.by import By
class onboardingLocators:
    onboardingButton = (By.ID, "viewOnboarding")
    letsCompleteButton = (By.ID, "obdLetsComplete")
    imageUploadButton = (By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.text-primary.mui-1w6h4uc")
    nextButton = (By.ID, "obdBtnNext")
    descriptionText = (By.XPATH, "//textarea[@name= 'businessDescription']")
    updateButton = (By.ID, "obdBtnUpdate")
    websiteText = (By.NAME, "websiteUrl")
    linkedInUrlText = (By.NAME, "linkedInUrl")
    twitterUrlText = (By.NAME, "twitterUrl")
    facebookUrlText = (By.NAME, "facebookUrl")
    skip_verify_account = (By.XPATH,"(//button[normalize-space()='Skip'])[1]")
    Topics = (By.XPATH, "(//span[normalize-space()='Adoption'])[1]")
    Primary = (By.XPATH, "(//span[normalize-space()='Automobile dealers, new only or new and used'])[1]")
    page_assertion = (By.XPATH, "(//h5[normalize-space()='Please tell us more about yourself'])[1]")
    imageUploadBusiness = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 text-primary mui-1w6h4uc']")
    next_button_primary = (By.XPATH, "//button[normalize-space()='Next']")
    closeButton = (By.ID, "obdBtnClose")
    tagline = (By.NAME, "tagline")
    snapchatUrlText = (By.NAME, "snapChatUrl")
    instgramUrlText = (By.NAME, "instagramUrl")
    titleText = (By.NAME, "title")
    projectDescription = (By.XPATH, "//textarea[@NAME='description']")
    projectUrl = (By.NAME, "projectUrl")
    descriptionInputText = (By.NAME, "businessOverviewDescription")
    updateButtonFreelance = (By.XPATH, "//button[normalize-space()='Update']")
    revenueText = (By.XPATH, "//input[@id='businessRevenue']")
    noOfEmployeesText = (By.XPATH, "//input[@id='noOfEmployees']")
    ownerShipText = (By.XPATH, "//div[@id='ownershipType']")
    ownerShipTypeText = (By.XPATH, "//li[@data-value='Private']")
    entityText = (By.XPATH, "//div[@id='entityType']")
    entityTypeText = (By.XPATH, "//li[@data-value='Independent']")
    headquaterText = (By.XPATH, "//div[@id='headquarter']")
    headquaterTypeText = (By.XPATH, "//li[@data-value='true']")
    foundedText = (By.XPATH, "//div[@id='founded']")
    foundedTypeText = (By.XPATH, "//li[@data-value='2018']")
    browse_button = (By.XPATH, "//button[@id='btn-browse']")
    browseoption_btn = (By.XPATH, "//li[@role='treeitem'][1]")
    subBrowseOption_btn = (By.XPATH, "//div[@class='MuiCollapse-wrapperInner MuiCollapse-vertical mui-8atqhb']//li["
                                     "@role='treeitem'][1]")
    checkboxForPrimaryIndustry = (By.XPATH, "//p[normalize-space()='Offices of Lawyers']")
    primaryChildText = (By.XPATH, '(//span[normalize-space()="Attorneys\' offices"])')
    donebBtn = (By.XPATH, "//button[@id='areaOfInterestBtnDone']")
    profileCompleteText = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl']")
    waitTextForLetsCompleteBtn = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and "
                                            "contains(text(),'Maximize')]")
    imagUploadingWait = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and  contains(text("
                                   "),'Please tell us')]")
    businessSummaryWait = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and  contains("
                                     "text(),'Business Summary')]")








