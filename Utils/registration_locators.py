from selenium.webdriver.common.by import By
class registrationLocators:
    signup_button = (By.XPATH, "(//a[normalize-space()='Sign Up'])[1]")
    Continue_button = (By.XPATH,"(//button[normalize-space()='Continue'])[1]")
    email_text = (By.XPATH,"//input[@name='username']")
    continue_2_button = (By.XPATH,"//button[@id=':r3:']")
    checkbox_1 = (By.XPATH, "//label[contains(@class, 'MuiFormControlLabel-root') and contains(@class, 'Mui-required')]")
    name_text = (By.XPATH, "//input[@name='firstName']")
    surname_text = (By.XPATH, "//input[@name='lastName']")
    newPassword_text = (By.XPATH, "//input[@name='password']")
    repeatPassword_text = (By.XPATH, "//input[@name='confirmPassword']")
    jobTitle_dropdown = (By.NAME, "jobTitle")
    jobTitle_option = (By.ID,":r2:-option-2")
    workplace_dropdown = (By.ID, ":r4:")
    workplace_option = (By.ID, ":r4:-option-0")
    start_date = (By.ID, ":r6:")
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




