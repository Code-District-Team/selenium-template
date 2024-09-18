import time

from selenium.webdriver import Keys


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Resources.businessInfo_data import businessInfoData



from selenium.webdriver.common.by import By


class tradelocators:
    profileAvtar = (By.ID, "profileAvatar")
    accountSettings = (By.XPATH, "//a[normalize-space()='Account Settings']")
    businessTab = (By.XPATH, "//button[normalize-space()='Business']")
    tradeTab = (By.XPATH, "//button[normalize-space()='Trade']")
    addMoreBrands = (By.XPATH, "(//button[normalize-space() = 'Add more'])[1]")
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
    carrierDropdown = (By.XPATH, "//input[contains(@class, 'MuiInputBase-input') and contains(@class, 'MuiAutocomplete-inputFocused')]")
    carrierDropdownOption = (By.XPATH, "//li[text()='DHL']")
    serviceDropdown = (By.XPATH, "(//input[contains(@class, 'MuiInputBase-input')])[3]")
    serviceDropdownOption = (By.XPATH, "//li[text()='Courier']")
    regionDropdown = (By.ID, "mui-component-select-geographicRegion")
    regionDropdownOption = (By.XPATH, "//li[normalize-space()='Africa']")
    incotermsDropdown = (By.XPATH, "(//input[contains(@class, 'MuiInputBase-input')])[4]")
    incotermsDropdownOption = (By.XPATH, "//li[@role='option' and text()='CIF']")
    addOriginAddress = (By.XPATH, "//p[text()='Origin Address']//following::button[1]")
    businessProfile = (By.XPATH, "//a[normalize-space()='Business Profile']")



class businesstrade:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_trade_tab(self):
        profileAvatar = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.profileAvtar))
        profileAvatar.click()
        accountSettings = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.accountSettings))
        accountSettings.click()
        businessTab = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.businessTab))
        businessTab.click()
        tradeTab = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.tradeTab))
        tradeTab.click()
        time.sleep(5)

    def add_brands(self):
        time.sleep(3)
        addBrandButton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(tradelocators.addMoreBrands))
        addBrandButton.click()
        selectBrand = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdown))
        selectBrand.click()
        selectBrandOption = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdownOption))
        selectBrandOption.click()
        saveBrand = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveBrand.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", addBrandButton)

    def addOriginAddress(self):
        addOrigin = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.addOriginAddress))
        addOrigin.click()
        countryDropdown = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.choseCountry))
        countryDropdown.click()
        time.sleep(5)
        countryDropdown.send_keys("Afghanistan")
        countryDropdown.send_keys(Keys.ENTER)
        stateDropdown = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.chooseState))
        stateDropdown.click()
        stateDropdownOption = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.chooseStateOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.cityInput))
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.zipCodeInput))
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.streetAddressInput))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveOriginAddress = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveOriginAddress.click()

    def addCurrency(self):
        addCurrency = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.addAcceptedCurrencyButton))
        addCurrency.click()
        addCurrencyDropdown = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.addMoreBrandsDropdown))
        addCurrencyDropdown.click()
        addCurrencyOption = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.addAcceptedCurrencyButtonOption))
        addCurrencyOption.click()
        saveCurrency = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveCurrency.click()

    def addNearestPort(self):
        addNearestPort = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.addNearestPortButton))
        addNearestPort.click()
        countryDropdown = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.choseCountry))
        countryDropdown.click()
        time.sleep(5)
        countryDropdown.send_keys("Afghanistan")
        countryDropdown.send_keys(Keys.ENTER)
        stateDropdown = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.chooseState))
        stateDropdown.click()
        stateDropdownOption = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.chooseStateOption))
        stateDropdownOption.click()
        cityInput = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.cityInput))
        cityInput.send_keys(businessInfoData.city)
        zipCode = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.zipCodeInput))
        zipCode.send_keys(businessInfoData.zipCode)
        streetAddress = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.streetAddressInput))
        streetAddress.send_keys(businessInfoData.streetAddress)
        saveOriginAddress = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveOriginAddress.click()

    def addDeliveryOption(self):
        addDeliveryButton = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.addDeliveryOption))
        addDeliveryButton.click()
        carrierDropdown = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.carrierDropdown))
        carrierDropdown.click()
        carrierDropdownOption = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.carrierDropdownOption))
        carrierDropdownOption.click()
        time.sleep(2)
        serviceDropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(tradelocators.serviceDropdown))
        serviceDropdown.click()
        serviceDropdownOption = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(tradelocators.serviceDropdownOption))
        serviceDropdownOption.click()
        regionDropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(tradelocators.regionDropdown))
        regionDropdown.click()
        regionDropdownOption = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.regionDropdownOption))
        regionDropdownOption.click()
        incontermsDropdown = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.incotermsDropdown))
        incontermsDropdown.click()
        incontermsDropdownOption = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(tradelocators.incotermsDropdownOption))
        incontermsDropdownOption.click()
        saveButton = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(tradelocators.saveButton))
        saveButton.click()

    def tradeInfo(self, driver):
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
