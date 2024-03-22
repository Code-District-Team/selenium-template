from selenium.webdriver.common.by import By
class registrationLocators:
    signup_button = (By.XPATH, "(//a[normalize-space()='Sign Up'])[1]")
    freelance_option = (By.XPATH, "//label[2]")
    business_basic_option = (By.XPATH, "//input[@value='businessFree']")
    Continue_button = (By.XPATH,"(//button[normalize-space()='Continue'])[1]")
    Continue_3_button = (By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[1]/form[1]/div[2]/button[2]")
    email_text = (By.XPATH,"//input[@name='username']")
    continue_2_button = (By.XPATH,"//button[@id=':r3:']")
    checkbox_1 = (By.XPATH, "//label[contains(@class, 'MuiFormControlLabel-root') and contains(@class, 'Mui-required')]")
    name_text = (By.XPATH, "//input[@name='firstName']")
    surname_text = (By.XPATH, "//input[@name='lastName']")
    newPassword_text = (By.XPATH, "//input[@name='password']")
    repeatPassword_text = (By.XPATH, "//input[@name='confirmPassword']")
    jobTitle_dropdown = (By.NAME, "jobTitle")
    jobTitle_option = (By.ID,":r2:-option-2")
    jobTitle_freelance = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/li[3]")
    otp_text_1 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 1'])[1]")
    otp_text_2 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 2'])[1]")
    otp_text_3 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 3'])[1]")
    otp_text_4 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 4'])[1]")
    otp_text_5 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 5'])[1]")
    otp_text_6 = (By.XPATH, "(//input[@aria-label='Please enter OTP character 6'])[1]")

    workplace_dropdown = (By.ID, ":r4:")
    selfemployeed_checkbox = (By.XPATH, "//span[@class='MuiTypography-root MuiTypography-body1 MuiFormControlLabel-label mui-1w6h4uc']")
    workplace_option = (By.ID, ":r4:-option-0")
    workplace_freelance_dropdown = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/input[1]")
    workplace_freelance_option = (By.XPATH, '/html[1]/body[1]/div[3]/div[1]/ul[1]/li[4]/div[2]/span[1]')
    start_date = (By.ID, ":r6:")
    start_date_freelance = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]")
    start_date_select = (By.XPATH, "//button[normalize-space()='13']")
    topics_browse = (By.XPATH, "(//button[normalize-space()='Browse'])[1]")
    select_topic_primary = (By.XPATH, "//p[normalize-space()='Life']")
    select_topic_2nd_tree = (By.XPATH, "//p[normalize-space()='Family']")
    checked_box_for_topics= (By.XPATH, "(//span[normalize-space()='Adoption'])[1]")
    Done_button = (By.XPATH, "//button[normalize-space()='Done']")
    country_dropdown = (By.NAME, "country")
    select_country = (By.CSS_SELECTOR, "li.MuiAutocomplete-option.MuiBox-root.mui-yxom3w.Mui-focused")
    state_dropdown = (By.ID, "mui-component-select-province")
    select_state = (By.XPATH, "//li[contains(text(),'Farāh (AF-FRA)')]")
    city_text = (By.XPATH, "(//input[@name='city'])[1]")
    zipcode_text = (By.XPATH, "(//input[@name='addressZip'])[1]")
    street_address_text = (By.XPATH, "(//input[@name='address1'])[1]")
    create_account_button = (By.CSS_SELECTOR, "button.MuiButton-root.btn-continue")
    description_box = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/textarea[1]")
    hourly_rate = (By.NAME, "hourlyRate")
    currency_dropdown = (By.XPATH, "//div[@id='mui-component-select-currency']")
    select_currency = (By.XPATH, "//li[contains(text(),'Costa Rica Colon (₡)')]")
    minimum_project_size = (By.NAME, "minProjectSize")
    availability_dropdown = (By.ID, "mui-component-select-availability")
    select_availability = (By.XPATH, "//li[normalize-space()='Full-Time']")
    browse_industries = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/button[1]")
    primary_option = (By.XPATH, "//li[@id=':r1q:-54']//div[@class='MuiTreeItem-iconContainer']//*[name()='svg']")
    create_freelance_account_button = (By.CSS_SELECTOR, "body > div:nth-child(17) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > button:nth-child(2)")

    verify_account = (By.XPATH, "(//h2[normalize-space()='Verify account'])[1]")
    business_plus_account = (By.XPATH, "//label[4]")
    seats_button = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium counter-icon mui-vubbuv'])[2]")

    continue_2_payment_screen = (By.ID, ":ro:")
