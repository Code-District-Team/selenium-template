import time

from selenium.webdriver.common.by import By
class busniness_registrationLocators:
    business_basic_option = (By.XPATH, "//label[3]")
    business_basic_dropdown = (By.XPATH, "//input[@id=':r1:']")
    email_input_field = (By.NAME, "businessEmail")
    company_name_input_field = (By.ID, "businessName")
    business_url = (By.ID, "businessUrl")
    continue_button = (By.ID, "addBusinessContinue")
    country_dropdown = (By.XPATH, "//input[@id=':r4:']")
    state_dropdown = (By.XPATH, "//div[@id='mui-component-select-province']")
    state_dropdown_option = (By.XPATH, "//li[contains(text(),'Badakhshān (AF-BDS)')]")
    city_input_field = (By.ID, "city")
    postalcode_input_field = (By.ID, "zip-code")
    street_address_input_field = (By.ID, "street-address")
    revenue_input_field = (By.ID, "revenue")
    company_size_input_field = (By.ID, "companySize")
    ownership_type_dropdown = (By.ID, "ownershipType")
    ownership_type_option = (By.XPATH, "//li[normalize-space()='Government']")
    entity_type_dropdown = (By.XPATH, "//div[@id='mui-component-select-entityType']")
    entity_type_option = (By.XPATH, "//li[normalize-space()='Parent']")
    headquarter_dropdown = (By.ID, "mui-component-select-headquarter")
    headquarter_dropdown_option = (By.XPATH, "//li[normalize-space()='Yes']")
    scroll_element = (By.XPATH, "//div[@class='MuiStack-root add-identity-fields mui-j7qwjs']")
    founded_year_dropdown = (By.ID, "mui-component-select-founded")
    founded_year_option = (By.XPATH, "//li[normalize-space()='2024']")
    browse_button = (By.ID, "btn-browse")
    primary_industry_parent_option = (By.XPATH, "//h6[@class='MuiTypography-root MuiTypography-h6 mui-1mopw5e' and .//span[1][text()='P'] and .//span[3][text()='r'] and .//span[5][text()='o']]")
    primary_industry_child_option = (By.XPATH, "(//p[normalize-space()='Legal Services (4)'])[1]")
    primary_industry_child_option_1 = (By.XPATH, "(//p[normalize-space()='Offices of Lawyers'])[1]")
    primary_industry_child_option_2 = (By.XPATH, '(//span[normalize-space()="Attorneys\' offices"])[1]')
    done_button = (By.ID, "areaOfInterestBtnDone")
    add_business = (By.ID, "addBusinessContinue")
    jobTitle_dropdown = (By.ID, ":ri:")
    jobTitle_option = (By.ID, ":ri:-option-0")
    startDate_field = (By.ID, ":rm:")
    startDate_option = (By.XPATH, "//button[normalize-space()='1']")
    addBusinessBtn = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 body1 mui-1w6h4uc']")






