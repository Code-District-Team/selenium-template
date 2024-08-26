import time

from selenium.webdriver import Keys


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.businessInfo_data import businessInfoData
from Pages.businessprofile.businessinfo import Businessinfo


from selenium.webdriver.common.by import By


class tradelocators:
    tradeTab = (By.XPATH, "//button[normalize-space()='Trade']")
    addMoreBrands = (By.XPATH, "//p[text()='Brands']//following::button[1]")
    addMoreBrandsDropdown = (By.ID, "tags-standard")
    addMoreBrandsDropdownOption = (By.ID, "tags-standard-option-0")
    saveButton = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
    addAcceptedCurrencyButton = (By.XPATH, "(//button[@type='button'][normalize-space()='Add more'])[3]")
    addAcceptedCurrencyButtonOption = (By.ID,"tags-standard-option-1")
    addNearestPortButton = (By.XPATH, "//p[text()='Nearest Port']//following::button[1]")
    choseCountry = (By.XPATH, "/html/body/div[5]/div[3]/div/div[2]/form/div[1]/div/div/input")
    chooseState = (By.ID, "mui-component-select-province")
    chooseStateOption = (By.XPATH, "//li[contains(text(),'Badakhshān (AF-BDS)')]")
    cityInput = (By.ID, "city")
    zipCodeInput = (By.ID, "zip-code")
    streetAddressInput = (By.ID, "street-address")
    addDeliveryOption = (By.XPATH, "(//button[@type='button'][normalize-space()='Add more'])[5]")
    carrierDropdown = (By.ID, "mui-component-select-carrier")
    carrierDropdownOption = (By.XPATH, "//li[normalize-space()='DHL']")
    serviceDropdown = (By.ID, "mui-component-select-service")
    serviceDropdownOption = (By.XPATH, "//li[normalize-space()='Courier']")
    regionDropdown = (By.ID, "mui-component-select-geographicRegion")
    regionDropdownOption = (By.XPATH, "//li[normalize-space()='Africa']")
    incotermsDropdown = (By.ID, "mui-component-select-incoterms")
    incotermsDropdownOption = (By.XPATH, "//li[normalize-space()='CIF']")
    addOriginAddress = (By.XPATH, "//p[text()='Origin Address']//following::button[1]")


class businesstrade:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_trade_tab(self):
        tradeTab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.tradeTab))
        tradeTab.click()

    def add_brands(self):
        time.sleep(3)
        addBrandButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(tradelocators.addMoreBrands))
        addBrandButton.click()
        selectBrand = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdown))
        selectBrand.click()
        selectBrandOption = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdownOption))
        selectBrandOption.click()
        saveBrand = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveBrand.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", addBrandButton)

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
        stateDropdownOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.chooseStateOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.cityInput))
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.zipCodeInput))
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.streetAddressInput))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveOriginAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveOriginAddress.click()

    def addCurrency(self):
        addCurrency = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.addAcceptedCurrencyButton))
        addCurrency.click()
        addCurrencyDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdown))
        addCurrencyDropdown.click()
        addCurrencyOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.addAcceptedCurrencyButtonOption))
        addCurrencyOption.click()
        saveCurrency = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveCurrency.click()

    def addNearestPort(self):
        addNearestPort = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(tradelocators.addNearestPortButton))
        addNearestPort.click()
        countryDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.choseCountry))
        countryDropdown.click()
        time.sleep(5)
        countryDropdown.send_keys("Afghanistan")
        countryDropdown.send_keys(Keys.ENTER)
        stateDropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.chooseState))
        stateDropdown.click()
        stateDropdownOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.chooseStateOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.cityInput))
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.zipCodeInput))
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.streetAddressInput))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveOriginAddress = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveOriginAddress.click()

    def addDeliveryOption(self):
        addDeliveryButton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.addDeliveryOption))
        addDeliveryButton.click()
        carrierDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.carrierDropdown))
        carrierDropdown.click()
        carrierDropdownOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.carrierDropdownOption))
        carrierDropdownOption.click()
        serviceDropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(tradelocators.serviceDropdown))
        serviceDropdown.click()
        serviceDropdownOption = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(tradelocators.serviceDropdownOption))
        serviceDropdownOption.click()
        regionDropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(tradelocators.regionDropdown))
        regionDropdown.click()
        regionDropdownOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.regionDropdownOption))
        regionDropdownOption.click()
        incontermsDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.incotermsDropdown))
        incontermsDropdown.click()
        incontermsDropdownOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tradelocators.incotermsDropdownOption))
        incontermsDropdownOption.click()
        saveButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveButton.click()

    def tradeInfo(self, driver):
        businessTab_instance = Businessinfo(driver)
        businessTab_instance.skip_account_verification()
        businessTab_instance.navigate_to_business_tab()
        self.navigate_to_trade_tab()
        time.sleep(5)
        self.add_brands()
        time.sleep(5)
        self.addOriginAddress()
        time.sleep(5)
        self.addCurrency()
        time.sleep(5)
        self.addNearestPort()
        time.sleep(5)
        self.addDeliveryOption()
