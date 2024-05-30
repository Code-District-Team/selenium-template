import time

from selenium.webdriver import Keys

from Utils.businessInfoLocators import businessInfoLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.businessInfo_data import businessInfoData




class Businessinfo:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_business_tab(self):
        businessTab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.businessTab))
        businessTab.click()
    def change_business_name(self):
        changeBusinessName = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.changeBusinessName))
        changeBusinessName.click()
        businessName = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.companyNameInput))
        businessName.clear()
        businessName.send_keys(businessInfoData.businessName)
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
        businessEmail.clear()
        businessEmail.send_keys(businessInfoData.businessEmail)
    def change_location(self):
        changeLocationButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.changeLocation))
        changeLocationButton.click()
        countryDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.changeBusinessName))
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
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.streetAddress))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveLocation = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(businessInfoLocators.saveLocation))
        saveLocation.click()
    def changeBusinessInfo(self):
        self.navigate_to_business_tab()
        self.change_business_name()
        self.change_business_contact()
        self.change_location()






