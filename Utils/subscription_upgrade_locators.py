from selenium.webdriver.common.by import By
class Subscriptionupgradelocators:

    account_settings_tab = (By.XPATH, "//a[normalize-space()='Account Settings']")
    subscription_tab = (By.XPATH, "//button[normalize-space()='Subscription']")
    upgrade_to_freelance_button = (By.XPATH, "(//button[normalize-space()='Upgrade to Freelancer'])[1]")
    button_continue = (By.XPATH, "//button[normalize-space()='Continue']")
    hourly_rate = (By.NAME, "hourlyRate")
    currency_dropdown_field = (By.XPATH, "//div[@id='mui-component-select-currency']")
    currency_dropdown_option = (By.XPATH, "//li[contains(text(),'Costa Rica Colon (₡)')]")
    minimum_project_size = (By.NAME, "minProjectSize")
    availability_dropdown = (By.ID, "mui-component-select-availability")
    availability_dropdown_option = (By.XPATH, "//li[normalize-space()='Full-Time']")
    continue_button = (By.ID, "regBtnContinue")
    chose_a_country_input = (By.ID, ":r1e:")
    state_field_dropdown = (By.ID, "mui-component-select-province")
    state_input_field_option = (By.XPATH, "//li[contains(text(),'Badakhshān (AF-BDS)')]")
    upgrade_subscription_button = (By.XPATH, "(//button[normalize-space()='Upgrade Subscription'])[1]")
    upgrade_to_business_basic = (By.XPATH, "(//button[normalize-space()='Upgrade to Business Basic'])[1]")
    upgrade_to_business_plus = (By.XPATH, "(//button[normalize-space()='Upgrade to Business Plus'])[1]")
    seat_increase_button = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium counter-icon mui-vubbuv'])[2]")
    click_to_continue = (By.ID, ":r12:")
    add_business_field = (By.XPATH, "//input[@class= 'MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused mui-1ev6tyo']")
    add_business_button = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 body1 mui-1w6h4uc']")
    country_dropdown = (By.XPATH, "/html[1]/body[1]/div[6]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    primary_industry_parent_option = (By.XPATH, "//h6[@class='MuiTypography-root MuiTypography-h6 mui-1mopw5e' and .//span[1][text()='P'] and .//span[3][text()='r'] and .//span[5][text()='o']]")
    primary_industry_child_option = (By.XPATH, "(//p[normalize-space()='Legal Services (4)'])[1]")
    primary_industry_child_option_1 = (By.XPATH, "(//p[normalize-space()='Offices of Lawyers'])[1]")
    primary_industry_child_option_2 = (By.XPATH, '(//span[normalize-space()="Attorneys\' offices"])[1]')
    continue_to_increase_seat = (By.ID, ":rf:")
    continue_button_business = (By.ID, "regBtnContinue")
    nextButton = (By.ID, "createAccount")
    closeButton = (By.XPATH, "//button[normalize-space()='Close']")
    currentSubscription = (By.XPATH, "//span[@class='MuiChip-label MuiChip-labelMedium mui-9iedg7']")
    downgradeToIndividual = (By.XPATH, '//*[@id="subsBtnDowngrade"]')
    confirmDowngrade = (By.XPATH, "//button[normalize-space()='Continue']")
    downgradeToBusinessBasic = (By.XPATH, "(//button[normalize-space()='Downgrade to Business Basic'])[1]")
    closeOnboardingModal = (By.XPATH, "//*[name()='path' and contains(@d,'M19 6.41 1')]")





