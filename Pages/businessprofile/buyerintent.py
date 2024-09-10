import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By


class buyerIntentLocators:
    profileAvtar = (By.ID, "profileAvatar")
    buyerProfile = (By.XPATH, "//li[normalize-space()='My Buyer Profile']")
    browserButton = (By.ID, "btn-browse")
    serviceTypeParentOption = (By.XPATH, "//h6[normalize-space()='Information (2)']")
    serviceTypeChildOption = (By.XPATH, "//p[normalize-space()='Data Processing, Hosting, and Related Services (1)']")
    serviceTypeChildOption_1 = (
    By.XPATH, "(//span[@class='MuiTypography-root MuiTypography-body1 MuiFormControlLabel-label mui-1w6h4uc'])[1]")
    doneButton = (By.ID, "areaOfInterestBtnDone")
    interestLevelInput = (By.ID, "mui-component-select-interestLevel")
    interestLevelOption = (By.XPATH, "//li[normalize-space()='Planning budgeting']")
    submitButton = (By.XPATH, "//button[@type='submit']")
    productTab = (By.XPATH, "//button[normalize-space()='Products']")
    productTabParentOption = (By.XPATH, "//h6[normalize-space()='Retail Trade (13)']")
    productTabChildOption = (By.XPATH, "(//p[normalize-space()='Other Motor Vehicle (3)'])[1]")
    productTabChildOption1 = (By.XPATH, "//span[normalize-space()='Recreational Vehicle']")
    deleteIcon = (By.XPATH, "//div[@class='table-actions MuiBox-root mui-0']//button[@type='button']//*[name()='svg']")
    deleteConfirmation = (By.XPATH, "//button[normalize-space()='Delete']")


class buyerintent:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_buyer_intent(self):
        time.sleep(70)
        userProfileAvatar = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.profileAvtar))
        userProfileAvatar.click()
        buyerProfile = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.buyerProfile))
        buyerProfile.click()
    def add_buyer_service(self):
        browserButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.browserButton))
        browserButton.click()
        browserServiceParent = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.serviceTypeParentOption))
        browserServiceParent.click()
        browserServiceChild = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.serviceTypeChildOption))
        browserServiceChild.click()
        browserServiceChild_1 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.serviceTypeChildOption_1))
        browserServiceChild_1.click()
        doneButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.doneButton))
        doneButton.click()
        interestLevelDropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.interestLevelInput))
        interestLevelDropdown.click()
        interestLevelDropdownOption = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.interestLevelOption))
        interestLevelDropdownOption.click()
        addService = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.submitButton))
        addService.click()
    def navigate_to_product_tab(self):
        productTab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.productTab))
        productTab.click()
    def delete_Intent(self):
         deleteIcon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.deleteIcon))
         deleteIcon.click()
         deleteConformation = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.deleteConfirmation))
         deleteConformation.click()
    def add_a_product(self):
        browserButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.browserButton))
        browserButton.click()
        browseProductParentOption = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.productTabParentOption))
        browseProductParentOption.click()
        browseProductChildOption = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.productTabChildOption))
        browseProductChildOption.click()
        browseProductChildOption1 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.productTabChildOption1))
        browseProductChildOption1.click()
        doneButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.doneButton))
        doneButton.click()
        interestLevelDropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.interestLevelInput))
        interestLevelDropdown.click()
        interestLevelDropdownOption = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.interestLevelOption))
        interestLevelDropdownOption.click()
        addService = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(buyerIntentLocators.submitButton))
        addService.click()
    def buyer_intent(self):
        time.sleep(5)
        self.navigate_to_buyer_intent()
        time.sleep(5)
        self.add_buyer_service()
        self.delete_Intent()
        time.sleep(5)
        self.navigate_to_product_tab()
        self.add_a_product()





