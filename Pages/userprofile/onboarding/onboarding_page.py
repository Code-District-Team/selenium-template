import os
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Utils.profile_locators import profileLocators

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
    waitTextForLetsCompleteBtn = (By.ID, "obdLetsComplete")
    imageUploadingWait = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and  contains(text("
                                   "),'Please tell us')]")
    businessSummaryWait = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 mui-14eb5wl' and  contains("
                                     "text(),'Business Summary')]")





class OnboardingPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_onboarding(self):
        profileAvatar = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(onboarding_Locators.profileAvtar))
        profileAvatar.click()
        clickToOnboarding = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboarding_Locators.restartOnboarding))
        clickToOnboarding.click()



    def click_lets_complete_button(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(onboarding_Locators.waitTextForLetsCompleteBtn))
        self.wait_and_click(onboarding_Locators.letsCompleteButton)


    def upload_button(self):
        self.wait_and_click(onboarding_Locators.imageUploadButton)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "profile.jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(2)

    def next_button(self):
        next_button = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(onboarding_Locators.nextButton))
        next_button.click()

    def page_assertion(self):
        page = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(onboarding_Locators.page_assertion))
        assert page.text == "Please tell us more about yourself"

    def description_field(self):
        description_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.descriptionText))
        description_field.send_keys("testing")

    def businessSummary_field(self):
        time.sleep(2)
        revenue_field = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboarding_Locators.revenueText))
        revenue_field.send_keys("400000")
        NoOfEmployees_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.noOfEmployeesText))
        NoOfEmployees_field.send_keys("200")
        ownership_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.ownerShipText))
        ownership_field.click()
        ownershipType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.ownerShipTypeText))
        ownershipType_field.click()
        entity_field = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboarding_Locators.entityText))
        entity_field.click()
        entityType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.entityTypeText))
        entityType_field.click()
        headQuaterText_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.headquaterText))
        headQuaterText_field.click()
        headQuaterType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.headQuaterTypeText))
        headQuaterType_field.click()
        foundedText_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.foundedText))
        foundedText_field.click()
        foundedType_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.foundedTypeText))
        foundedType_field.click()

    def primaryIndustry_field(self):
        browse_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.browse_button))
        browse_field.click()
        browseOption_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.browseOption_btn))
        browseOption_field.click()

        subBrowseOption_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.subBrowseOption_btn))
        subBrowseOption_field.click()

        subBrowseOption_field_ = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.checkboxForPrimaryIndustry))
        subBrowseOption_field_.click()

        primaryIndustryChild_field_ = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.primaryChildText))
        primaryIndustryChild_field_.click()
        time.sleep(5)

        doneBtn_field = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.doneBtn))
        doneBtn_field.click()

    def update_button(self):
        self.wait_and_click(onboarding_Locators.updateButton)
        time.sleep(2)

    def website_url(self):
        websiteText = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboarding_Locators.websiteText))
        websiteText.send_keys("https://www.codedistrict.com")

    def linkedIn_Url_Text(self):
        linkedInUrlText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.linkedInUrlText))
        linkedInUrlText.send_keys("https://www.linkedin.com/in/asadhafeez15")

    def twitter_Url_Text(self):
        twitterUrlText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.twitterUrlText))
        twitterUrlText.send_keys("https://x.com/asadhafeez_")

    def facebook_Url_Text(self):
        facebookUrlText = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(onboarding_Locators.facebookUrlText))
        facebookUrlText.send_keys("https://www.facebook.com/asad.hafeez.942/")

    def skip_verify(self):
        self.wait_and_click(onboarding_Locators.skip_verify_account)

    def business_logo_upload(self):
        self.wait_and_click(onboarding_Locators.imageUploadBusiness)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Profile image', "images (1).jpg")
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(2)

    def next_button_1(self):
        self.wait_and_click(onboarding_Locators.next_button_primary)

    def close_button(self):
        self.wait_and_click(onboarding_Locators.closeButton)

    def tagline(self):
        tagline = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(onboarding_Locators.tagline))
        tagline.send_keys("We are dreamers")

    def wait_and_click(self, locator):
        print(f"Waiting for element {locator} to be clickable...")
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        print(f"Element {locator} found. Clicking it now.")
        element.click()

    def wait_locator(self,locator):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

    def onboarding_start(self):
        self.navigate_to_onboarding()
        self.click_lets_complete_button()
        self.upload_button()
        self.next_button()
        self.wait_locator(onboarding_Locators.imageUploadingWait)
        self.next_button()
        time.sleep(5)
        self.next_button()
        self.business_logo_upload()
        self.next_button()
        self.description_field()
        self.next_button()
        self.wait_locator(onboarding_Locators.businessSummaryWait)
        self.businessSummary_field()
        self.next_button()
        time.sleep(5)
        # self.primaryIndustry_field()
        time.sleep(5)
        self.next_button_1()

        self.next_button()
        time.sleep(10)
        self.next_button()
        self.website_url()
        self.linkedIn_Url_Text()
        self.twitter_Url_Text()
        self.facebook_Url_Text()
        self.update_button()
        self.close_button()
