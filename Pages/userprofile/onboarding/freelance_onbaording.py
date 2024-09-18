import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.userprofile.onboarding.onboarding_page import OnboardingPage
import mouseinfo
class onboarding_Locators:
    profileAvtar = (By.XPATH, "//div[@id='profileAvatar']//*[name()='svg']")
    restartOnboarding = (By.XPATH,"//li[normalize-space()='Restart Onboarding']")
    letsCompleteButton = (By.ID, "obdLetsComplete")
    imageUploadButton = (By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.text-primary.mui-1w6h4uc")
    nextButton = (By.ID, "obdBtnNext")
    descriptionText = (By.XPATH, "//textarea[@name= 'businessDescription']")
    updateButton = (By.ID, "obdBtnUpdate")
    websiteText = (By.NAME, "websiteUrl")
    linkedInUrlText = (By.NAME, "linkedInUrl")
    twitterUrlText = (By.NAME, "twitterUrl")
    facebookUrlText = (By.NAME, "facebookUrl")
    skip_verify_account = (By.XPATH, "(//button[normalize-space()='Skip'])[1]")
    Topics = (By.XPATH, "(//span[normalize-space()='Adoption'])[1]")
    Primary = (By.XPATH, "(//span[normalize-space()='Automobile dealers, new only or new and used'])[1]")
    page_assertion = (By.XPATH, "(//h5[normalize-space()='Please tell us more about yourself'])[1]")
    imageUploadBusiness = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 text-primary mui-1w6h4uc']")
    next_button_primary = (By.XPATH, "//button[normalize-space()='Next']")
    closeButton = (By.ID, "obdBtnClose")
    tagline = (By.NAME, "tagline")
    snapchatUrlText = (By.NAME, "snapChatUrl")
    instagramUrlText = (By.NAME, "instagramUrl")
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
    headQuaterTypeText = (By.XPATH, "//li[@data-value='true']")
    foundedText = (By.XPATH, "//div[@id='founded']")
    foundedTypeText = (By.XPATH, "//li[@data-value='2018']")
    browse_button = (By.XPATH, "//button[@id='btn-browse']")
    browseOption_btn = (By.XPATH, "//li[@role='treeitem'][1]")
    subBrowseOption_btn = (By.XPATH, "//div[@class='MuiCollapse-wrapperInner MuiCollapse-vertical mui-8atqhb']//li["
                                     "@role='treeitem'][1]")
    checkboxForPrimaryIndustry = (By.XPATH, "//p[normalize-space()='Offices of Lawyers']")
    primaryChildText = (By.XPATH, '(//span[normalize-space()="Attorneys\' offices"])')
    doneBtn = (By.XPATH, "//button[@id='areaOfInterestBtnDone']")
    profileCompleteText = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl']")
    waitTextForLetsCompleteBtn = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and "
                                            "contains(text(),'Maximize')]")
    imageUploadingWait = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and  contains(text("
                                   "),'Please tell us')]")
    businessSummaryWait = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and  contains("
                                     "text(),'Business Summary')]")


class FreelanceOnboardingPage:
    def __init__(self, driver):
        self.driver = driver

    def snapchatUrl(self):
        snapchatUrl = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.snapchatUrlText))
        snapchatUrl.send_keys("https://www.snapchat.com/add/asad_hafeez?share_id=9zDzsurRCVE&locale=en-GB")

    def instagramUrl(self):
        instagramUrl = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.instagramUrlText))
        instagramUrl.send_keys("https://www.instagram.com/asadhafeez_/")

    def projecttitle(self):
        tileText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboarding_Locators.titleText))
        tileText.send_keys("Eat and sleep")

    def description(self):
        descriptionText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.projectDescription))
        descriptionText.send_keys("This is my test project")

    def projecturl(self):
        projectURL = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboarding_Locators.projectUrl))
        projectURL.send_keys("https://development.d2vtpkgl21lrum.amplifyapp.com/")

    def businessdescription(self):
        businessOverviewDescription = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.descriptionInputText))
        businessOverviewDescription.send_keys("Lets do it")
        time.sleep(3)

    def updatebutton(self):
        updateButton = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.updateButtonFreelance))
        updateButton.click()

    def freelanceonboarding(self, driver_setup):
        onboarding_page_instance = OnboardingPage(driver_setup)
        onboarding_page_instance.navigate_to_onboarding()
        time.sleep(2)
        onboarding_page_instance.click_lets_complete_button()
        onboarding_page_instance.upload_button()
        time.sleep(6)
        onboarding_page_instance.tagline()
        onboarding_page_instance.website_url()
        onboarding_page_instance.linkedIn_Url_Text()
        onboarding_page_instance.twitter_Url_Text()
        onboarding_page_instance.facebook_Url_Text()
        self.instagramUrl()
        self.snapchatUrl()
        onboarding_page_instance.next_button_1()
        time.sleep(1)
        onboarding_page_instance.next_button()
        time.sleep(1)
        onboarding_page_instance.next_button()
        time.sleep(1)
        onboarding_page_instance.business_logo_upload()
        self.projecttitle()
        time.sleep(1)
        self.description()
        time.sleep(1)
        self.projecturl()
        onboarding_page_instance.next_button_1()
        time.sleep(1)
        self.businessdescription()
        self.updatebutton()
        time.sleep(5)
        onboarding_page_instance.close_button()
        time.sleep(5)

        # freelanceToast_alert = WebDriverWait(self.driver, 30).until(
        #     EC.visibility_of_element_located(profileLocators.businessAlert))
        # actual_loginToast_text = freelanceToast_alert.text
        # expected_loginToast_text = "Profile updated successfully"
        # assert actual_loginToast_text == expected_loginToast_text, f"Expected '{expected_loginToast_text}', but got '{actual_loginToast_text}'"

        # profileCompletion = WebDriverWait(self.driver, 30).until(
        #     EC.visibility_of_element_located(onboardingLocators.profileCompleteText))
        # actual_text = profileCompletion.text
        # expected_text = "Your profile is 100% complete"
        # assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
