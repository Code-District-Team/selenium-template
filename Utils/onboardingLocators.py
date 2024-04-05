from selenium.webdriver.common.by import By
class onboardingLocators:
    onboardingButton = (By.XPATH, "//button[normalize-space()='Re-start onboarding']")
    letsCompleteButton = (By.XPATH, "//div[@role='presentation']//button[2]")
    imageUploadButton = (By.XPATH, "(//div[@class='MuiBox-root mui-0'])[4]")
    nextButton = (By.XPATH, "(//button[normalize-space()='Next'])[1]")
    descriptionText = (By.XPATH, "//textarea[@name= 'businessDescription']")
    updateButton = (By.XPATH, "(//button[normalize-space()='Update'])[1]")
    websiteText = (By.XPATH, "(//input[@name='websiteUrl'])[1]")
    linkedInUrlText = (By.XPATH, "(//input[@name='linkedInUrl'])[1]")
    twitterUrlText = (By.XPATH, "(//input[@name='twitterUrl'])[1]")
    facebookUrlText = (By.XPATH, "(//input[@name='facebookUrl'])[1]")
    skip_verify_account = (By.XPATH,"(//button[normalize-space()='Skip'])[1]")
    Topics = (By.XPATH, "(//span[normalize-space()='Adoption'])[1]")
    Primary = (By.XPATH, "(//span[normalize-space()='Automobile dealers, new only or new and used'])[1]")
    page_assertion = (By.XPATH, "(//h5[normalize-space()='Please tell us more about yourself'])[1]")





