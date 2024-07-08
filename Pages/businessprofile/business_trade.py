+import time

from selenium.webdriver import Keys

from Utils.tradeTabLocators import tradelocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.businessInfo_data import businessInfoData
from Pages.businessprofile.businessinfo import Businessinfo

class businesstrade:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_trade_tab(self):
        tradeTab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.tradeTab))
        tradeTab.click()
    def add_brands(self):
        addBrandButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.addMoreBrands))
        addBrandButton.click()
        selectBrand = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdown))
        selectBrand.click()
        selectBrandOption = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdownOption))
        selectBrandOption.click()
        saveBrand = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveBrand.click()
    def addOriginAddress(self):
        addOrigin = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.addOriginAddress))
        addOrigin.click()
        countryDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.choseCountry))
        countryDropdown.click()
        time.sleep(5)
        countryDropdown.send_keys("Afghanistan")
        countryDropdown.send_keys(Keys.ENTER)
        stateDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.chooseState))
        stateDropdown.click()
        stateDropdownOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.chooseStateOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.cityInput))
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.zipCodeInput))
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.streetAddressInput))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveOriginAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveOriginAddress.click()
    def addCurrency(self):
        addCurrency = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.addAcceptedCurrencyButton))
        addCurrency.click()
        addCurrencyDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdown))
        addCurrencyDropdown.click()
        addCurrencyOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.addAcceptedCurrencyButtonOption))
        addCurrencyOption.click()
        saveCurrency = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveCurrency.click()
    def addNearestPort(self):
        addNearestPort = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.addNearestPortButton))
        addNearestPort.click()
        countryDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.choseCountry))
        countryDropdown.click()
        time.sleep(5)
        countryDropdown.send_keys("Afghanistan")
        countryDropdown.send_keys(Keys.ENTER)
        stateDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.chooseState))
        stateDropdown.click()
        stateDropdownOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.chooseStateOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.cityInput))
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.zipCodeInput))
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.streetAddressInput))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveOriginAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveOriginAddress.click()
    def addDeliveryOption(self):
        addDeliveryButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.addDeliveryOption))
        addDeliveryButton.click()
        carrierDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.carrierDropdown))
        carrierDropdown.click()
        carrierDropdownOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.carrierDropdownOption))
        carrierDropdownOption.click()
        serviceDropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(tradelocators.serviceDropdown))
        serviceDropdown.click()
        serviceDropdownOption = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(tradelocators.serviceDropdownOption))
        serviceDropdownOption.click()
        regionDropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(tradelocators.regionDropdown))
        regionDropdown.click()
        regionDropdownOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.regionDropdownOption))
        regionDropdownOption.click()
        incontermsDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.incotermsDropdown))
        incontermsDropdown.click()
        incontermsDropdownOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.incotermsDropdownOption))
        incontermsDropdownOption.click()
        saveButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveButton.click()
    def tradeInfo(self, driver):
        businessTab_instance = Businessinfo(driver)
        businessTab_instance.skip_account_verification()
        businessTab_instance.skip_account_verification()
        businessTab_instance.navigate_to_business_tab()
        self.navigate_to_trade_tab()
        time.sleep(10)
        self.add_brands()
        self.addOriginAddress()
        time.sleep(10)
        self.addCurrency()
        time.sleep(10)
        self.addNearestPort()
        time.sleep(10)
        self.addDeliveryOption()




