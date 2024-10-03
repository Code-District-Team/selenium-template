
from selenium.webdriver import Keys

from Resources.registration_data import RegistrationTestData
from Resources.business_registration_data import business_registrationTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.userprofile.Registration.Individual_registration_page import RegistrationPage

import time

from selenium.webdriver.common.by import By


class registrationLocators:


    signup_button = (By.ID, "btnJoinForFree")
    freelance_option = (By.XPATH, "//label[2]")
    business_basic_option = (By.XPATH, "//input[@value='businessFree']")
    continue_button = (By.ID,"regBtnContinue")

    email_text = (By.ID,"userEmail")

    checkbox_1 = (By.XPATH, "//label[contains(@class, 'MuiFormControlLabel-root') and contains(@class, 'Mui-required')]")
    name_text = (By.ID, "personalName")
    surname_text = (By.ID, "surname")
    newPassword_text = (By.NAME, "password")
    repeatPassword_text = (By.NAME, "confirmPassword")
    jobTitle_input = (By.XPATH, "//input[@placeholder='Search your job title here']")
    otp_text_1 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 1'])[1]")
    otp_text_2 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 2'])[1]")
    otp_text_3 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 3'])[1]")
    otp_text_4 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 4'])[1]")
    otp_text_5 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 5'])[1]")
    otp_text_6 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 6'])[1]")

    workplace_dropdown = (By.XPATH, "//div[starts-with(@class,'MuiAutocomplete') and @name='businessId']//div[starts-with(@class,'MuiInputBase')]//input")
    selfemployeed_checkbox = (By.XPATH, "//span[@class='MuiTypography-root MuiTypography-body1 MuiFormControlLabel-label mui-1w6h4uc']")
    start_date = (By.XPATH, "//input[@placeholder='MMMM YYYY' and @type='text' ]")
    start_month = (By.XPATH, "//button[normalize-space()='Jul']")
    start_date_year = (By.XPATH, "//button[normalize-space()='2024']")
    browse_button = (By.XPATH, "(//button[@id='btn-browse'])[1]")
    select_topic_primary = (By.XPATH, "//h6[normalize-space()='Life (6)']")
    select_topic_2nd_tree = (By.XPATH, "//p[normalize-space()='Family (8)']")
    checked_box_for_topics = (By.XPATH, "//span[normalize-space()='Adoption']")
    Done_button = (By.ID, "areaOfInterestBtnDone")
    country_dropdown = (By.NAME, "country")
    select_country = (By.CSS_SELECTOR, "li.MuiAutocomplete-option.MuiBox-root.mui-yxom3w.Mui-focused")
    state_dropdown = (By.ID, "mui-component-select-province")
    select_state = (By.XPATH, "//li[contains(text(),'Farāh (AF-FRA)')]")
    city_text = (By.ID, "city")
    zipcode_text = (By.ID, "zip-code")
    street_address_text = (By.ID, "street-address")
    create_account_button = (By.ID, "createAccount")
    description_box = (By.ID, "regFreelanceDescription")
    hourly_rate = (By.NAME, "hourlyRate")
    currency_dropdown = (By.ID, "mui-component-select-currency")
    select_currency = (By.XPATH, "(//li[contains(text(),'Afghanistan Afghani (؋)')])[1]")
    minimum_project_size = (By.NAME, "minProjectSize")
    availability_dropdown = (By.ID, "mui-component-select-availability")
    select_availability = (By.XPATH, "//li[normalize-space()='Full-Time']")
    continue_button_freelance = (By.XPATH,"//button[normalize-space()='Continue']")
    primary_option = (By.XPATH, "//li[@id=':r1q:-54']//div[@class='MuiTreeItem-iconContainer']//*[name()='svg']")

    verify_account = (By.XPATH, "(//h2[normalize-space()='Verify account'])[1]")
    business_plus_account = (By.XPATH, "//label[4]")
    seats_button = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium counter-icon mui-vubbuv'])[2]")
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
    jobTitle_dropdown = (By.XPATH, "//input[@placeholder='Search your job title here']")
    jobTitle_option = (By.ID, ":ri:-option-0")
    startDate_field = (By.ID, ":rm:")
    startDate_option = (By.XPATH, "//button[normalize-space()='1']")
    addBusinessBtn = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 body1 mui-1w6h4uc']")



class BusinessBasicRegistration:
    payment_processing: object

    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(registrationLocators.signup_button))
        signup_button.click()

    time.sleep(3)

    def select_business_basic_option(self):
        business_basic_option = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.business_basic_option))
        business_basic_option.click()



    def add_business(self):
        business_dropdown = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.business_basic_dropdown))
        business_dropdown.send_keys("code")
        add_business = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(busniness_registrationLocators.addBusinessBtn))
        add_business.click()
        enter_email = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(busniness_registrationLocators.email_input_field))
        enter_email.send_keys(business_registrationTestData.business_email)
        enter_company_name = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.company_name_input_field))
        enter_company_name.send_keys(business_registrationTestData.business_name)
        enter_business_url = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.business_url))
        enter_business_url.send_keys(business_registrationTestData.business_url)
        continue_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        country_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(busniness_registrationLocators.country_dropdown))
        country_dropdown.click()
        time.sleep(3)
        country_dropdown.send_keys(business_registrationTestData.country_name)
        country_dropdown.send_keys(Keys.ENTER)
        state_dropdown = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown))
        state_dropdown.click()
        state_dropdown_option = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.state_dropdown_option))
        state_dropdown_option.click()
        city_name = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.city_input_field))
        city_name.click()
        city_name.send_keys(business_registrationTestData.city_name)
        postal_code = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.postalcode_input_field))
        postal_code.click()
        postal_code.send_keys(business_registrationTestData.postalcode)
        street_address = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.street_address_input_field))
        street_address.click()
        street_address.send_keys(business_registrationTestData.street_address)
        continue_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()

        revenue_input = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.revenue_input_field))
        revenue_input.send_keys(business_registrationTestData.revenue)
        company_size = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.company_size_input_field))
        company_size.send_keys(business_registrationTestData.company_size)
        ownership_type_dropdown = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_dropdown))
        ownership_type_dropdown.click()
        ownership_type_option = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.ownership_type_option))
        ownership_type_option.click()
        entity_type_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(busniness_registrationLocators.entity_type_dropdown))
        entity_type_dropdown.click()
        entity_type_option = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.entity_type_option))
        entity_type_option.click()
        time.sleep(2)
        founded_year_dropdown = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.founded_year_dropdown))
        founded_year_dropdown.click()
        founded_year_option = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(busniness_registrationLocators.founded_year_option))
        founded_year_option.click()
        time.sleep(2)
        continue_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()
        time.sleep(3)
        primary_industry_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.browse_button))
        primary_industry_button.click()
        primary_industry_parent_option = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_parent_option))
        primary_industry_parent_option.click()
        primary_industry_child_option = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option))
        primary_industry_child_option.click()
        primary_industry_child_option_1 = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option_1))
        primary_industry_child_option_1.click()
        primary_industry_child_option_2 = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.primary_industry_child_option_2))
        primary_industry_child_option_2.click()
        primary_industry_done = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.done_button))
        primary_industry_done.click()
        continue_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.continue_button))
        continue_button.click()

        add_business = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(busniness_registrationLocators.add_business))
        add_business.click()

    def continue_button_click(self):
        continue_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(registrationLocators.continue_button))
        continue_button.click()

    def enter_email(self, email_address):  # Corrected method signature here
        email_field = WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located(registrationLocators.email_text))
        email_field.send_keys(email_address)  # Corrected parameter name here

    def click_checkbox(self):
        checkbox_1 = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(registrationLocators.checkbox_1))
        checkbox_1.click()

    def personal_info(self):
        name = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(registrationLocators.name_text))
        name.send_keys(RegistrationTestData.username)
        surname = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(registrationLocators.surname_text))
        surname.send_keys(RegistrationTestData.surname)
        password = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(registrationLocators.newPassword_text))
        password.send_keys(RegistrationTestData.password)
        repeat_password = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(registrationLocators.repeatPassword_text))
        repeat_password.send_keys(RegistrationTestData.password)


    def create_account_button(self):
        create_account_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(registrationLocators.create_account_button))
        create_account_button.click()

    def otp(self, otp_digits):
        signup_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(registrationLocators.otp_text_1))
        signup_button.send_keys(otp_digits)
    def jobTitle(self):
        job_title_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(registrationLocators.jobTitle_input))
        job_title_dropdown.click()
        job_title_dropdown.send_keys(".Net Architect")
        job_title_dropdown.send_keys(Keys.RETURN)
        start_date = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(registrationLocators.start_date))
        start_date.click()
        start_date_year = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(registrationLocators.start_date_year))
        start_date_year.click()
        start_month = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(registrationLocators.start_month))
        self.driver.execute_script("arguments[0].click();", start_month)

    def signup_basic_business(self, driver):
        isinstance_registration = RegistrationPage(driver)
        isinstance_registration.click_signup_button()
        self.select_business_basic_option()
        isinstance_registration.click_continue_button()
        self.add_business()
        isinstance_registration.click_continue_button()
        isinstance_registration.enter_email()
        isinstance_registration.click_checkbox()
        isinstance_registration.click_continue_button()
        isinstance_registration.personal_info()
        isinstance_registration.click_continue_button()
        self.jobTitle()
        isinstance_registration.click_continue_button()
        isinstance_registration.select_topic()
        isinstance_registration.click_continue_button()
        isinstance_registration.select_address()
        isinstance_registration.create_account_button()
        isinstance_registration.otp()
        isinstance_registration.click_continue_button()
        time.sleep(15)

