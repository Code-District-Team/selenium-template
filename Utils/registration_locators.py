from selenium.webdriver.common.by import By
import faker as Faker



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
    jobTitle_freelance = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/li[3]")
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

