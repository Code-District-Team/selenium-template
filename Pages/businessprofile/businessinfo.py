import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webelement import WebElement

from Utils.businessInfoLocators import businessInfoLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.businessInfo_data import businessInfoData




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
        businessTab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.businessTab))
        businessTab.click()
    def change_business_name(self):
        changeBusinessName = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(businessInfoLocators.changeBusinessName))
        changeBusinessName.click()
        businessName: WebElement = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(businessInfoLocators.companyNameInput))
        time.sleep(2)
        businessName.send_keys(Keys.CONTROL, 'a')  # Select all text
        businessName.send_keys(Keys.DELETE)
        time.sleep(2)
        businessName.send_keys("ABCRRR")
        saveButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.companyNameSave))
        saveButton.click()
    def change_business_contact(self):
        changeRevenueButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.changeBusinessContact))
        changeRevenueButton.click()
        businessContactInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.businessContact))
        businessContactInput.send_keys(businessInfoData.businessContact)
        businessFax = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.businessContactFax))
        businessFax.send_keys(businessInfoData.businessFax)
        businessEmail = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.businessEmail))
        time.sleep(2)
        businessEmail.send_keys(Keys.CONTROL, 'a')  # Select all text
        businessEmail.send_keys(Keys.DELETE)
        time.sleep(2)
        businessEmail.send_keys(businessInfoData.businessEmail)
        saveBtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.saveLocation))
        saveBtn.click()
    def change_location(self):
        changeLocationButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.changeLocation))
        changeLocationButton.click()
        countryDropdown = WebDriverWait(self.driver, 70).until(EC.element_to_be_clickable(businessInfoLocators.countryDropdown))
        countryDropdown.click()
        time.sleep(15)
        countryDropdown.send_keys(businessInfoData.countryName)
        countryDropdown.send_keys(Keys.ENTER)
        stateDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.stateDropdown))
        stateDropdown.click()
        stateDropdownOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.stateDropdownOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.cityInput))
        cityInput.clear()
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.zipCode))
        time.sleep(2)
        zipCode.send_keys(Keys.CONTROL, 'a')  # Select all text
        zipCode.send_keys(Keys.DELETE)
        time.sleep(2)
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.streetAddress))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveLocation = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.saveLocation))
        saveLocation.click()
    def changeBusinessInfo(self):
        self.navigate_to_business_tab()
        time.sleep(10)
        self.change_business_name()
        time.sleep(10)
        self.change_business_contact()
        time.sleep(10)
        self.change_location()






