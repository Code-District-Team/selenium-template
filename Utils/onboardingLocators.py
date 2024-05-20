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
    projectDescription = (By.NAME, "description")
    projectUrl = (By.NAME, "projectUrl")
    descriptionInputText = (By.NAME, "businessOverviewDescription")
    updateButtonFreelance = (By.XPATH, "//button[normalize-space()='Update']")







