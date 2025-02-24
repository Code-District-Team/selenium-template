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















