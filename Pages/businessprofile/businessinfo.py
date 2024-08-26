import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.businessInfo_data import businessInfoData
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


class Businessinfo:
    def __init__(self, driver):
        self.driver = driver

    def skip_account_verification(self, skipAccouWHntVerification=None):
        global skipAccountVerification
        try:
            skipAccountVerification = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(businessInfoLocators.skipAccountVerification)
            )

            # Scroll to the element
            self.driver.execute_script("arguments[0].scrollIntoView(true);", skipAccountVerification)
            time.sleep(1)  # Give some time for scrolling to complete

            # Attempt to click using ActionChains
            actions = ActionChains(self.driver)
            actions.move_to_element(skipAccountVerification).click().perform()

        except ElementClickInterceptedException:
            print("ElementClickInterceptedException encountered. Trying JavaScript click...")
            # Perform click using JavaScript as a fallback
            self.driver.execute_script("arguments[0].click();", skipAccouWHntVerification)
        except TimeoutException as e:
            print(f"TimeoutException: {e}")
        except Exception as e:
            print(f"An unexpected exception occurred: {e}")

    def navigate_to_business_tab(self):
        avatarTab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.avatar))
        avatarTab.click()
        settingsclick = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.accountsettingbtn))
        settingsclick.click()
        businessTab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.businessTab))
        businessTab.click()

    def change_business_name(self):
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, "//p[text("
                                                                                                        ")='Company "
                                                                                                        "Name']"))
        changeBusinessName = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(businessInfoLocators.changeBusinessName))
        changeBusinessName.click()
        businessName: WebElement = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(businessInfoLocators.companyNameInput))
        time.sleep(2)
        businessName.send_keys(Keys.CONTROL, 'a')  # Select all text
        businessName.send_keys(Keys.DELETE)
        time.sleep(2)
        businessName.send_keys("Fenty Beauty")
        saveButton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.companyNameSave))
        saveButton.click()

    def change_business_contact(self):
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, "//p[text()='Contact']"))
        changeRevenueButton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.changeBusinessContact))
        changeRevenueButton.click()
        businessContactInput = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.businessContact))
        businessContactInput.send_keys(businessInfoData.businessContact)
        businessFax = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.businessContactFax))
        businessFax.send_keys(businessInfoData.businessFax)
        businessEmail = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.businessEmail))
        ##time.sleep(2)
        businessEmail.send_keys(Keys.CONTROL, 'a')
        businessEmail.send_keys(Keys.DELETE)
        #time.sleep(2)
        businessEmail.send_keys(businessInfoData.businessEmail)
        saveBtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.saveLocation))
        saveBtn.click()

    def change_location(self):
        changeLocationButton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.changeLocation))
        changeLocationButton.click()
        countryDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.countryDropdown))
        countryDropdown.click()
        #time.sleep(5)
        countryDropdown.send_keys(businessInfoData.countryName)
        countryDropdown.send_keys(Keys.ENTER)
        stateDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.stateDropdown))
        stateDropdown.click()
        stateDropdownOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.stateDropdownOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.cityInput))
        cityInput.clear()
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.zipCode))
        #time.sleep(2)
        zipCode.send_keys(Keys.CONTROL, 'a')  # Select all text
        zipCode.send_keys(Keys.DELETE)
        #time.sleep(2)
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.streetAddress))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveLocation = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(businessInfoLocators.saveLocation))
        saveLocation.click()

    def changeBusinessInfo(self):
        self.navigate_to_business_tab()
        self.change_business_name()
        self.change_business_contact()
        self.change_location()
