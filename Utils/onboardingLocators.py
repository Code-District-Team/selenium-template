from selenium.webdriver.common.by import By
class onboardingLocators:
    onboardingButton = (By.XPATH, "//button[normalize-space()='Re-start onboarding']")
    letsCompleteButton = (By.XPATH, "(//button[normalize-space()='Let's complete'])[1]")
    imageUploadButton = (By.XPATH, "(//div[@class='MuiBox-root mui-0'])[4]")
    nextButton = (By.XPATH, "(//button[normalize-space()='Next'])[1]")
    descriptionText = (By.XPATH, "(//textarea[@id=':ri:'])[1]")
    updateButton = (By.XPATH, "(//button[normalize-space()='Update'])[1]")
    websiteText = (By.XPATH, "(//input[@name='websiteUrl'])[1]")
    linkedInUrlText = (By.XPATH, "(//input[@name='linkedInUrl'])[1]")
    twitterUrlText = (By.XPATH, "(//input[@name='twitterUrl'])[1]")
    facebookUrlText = (By.XPATH, "(//input[@name='facebookUrl'])[1]")




