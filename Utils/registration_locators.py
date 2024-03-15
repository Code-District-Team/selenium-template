from selenium.webdriver.common.by import By
class registrationLocators:
    signup_button = (By.XPATH, "(//a[normalize-space()='Sign Up'])[1]")
    Continue_button = (By.XPATH,"(//button[normalize-space()='Continue'])[1]")
    email_text = (By.XPATH,"//input[@name='username']")
    continue_2_button = (By.XPATH,"//button[@id=':r3:']")
    checkbox_1 = (By.XPATH, "input[value='false'][name='opsNotificationConsent']")
    name_text = (By.XPATH, "//input[@name='firstName']")
    surname_text = (By.XPATH, "//input[@name='lastName']")
    newPassword_text = (By.XPATH, "//input[@name='password']")
    repeatPassword_text = (By.XPATH, "//input[@name='confirmPassword']")
    jobTitle_dropdown = (By.XPATH, "//input[@id=':r4:']")
    jobTitle_option = (By.ID,":r4:-option-3")
    workplace_dropdown = (By.XPATH, "//input[@id=':r6:']")
    workplace_option = (By.ID, ":r6:-option-0")
    start_date = (By.ID, ":r8:")
    start_date_select = (By.XPATH, "//button[normalize-space()='13']")
    topics_browse = (By.XPATH, "//button[normalize-space()='Browse']")
    select_topic_primary = (By.XPATH, "//p[normalize-space()='Life']")
    select_topic_2nd_tree = (By.XPATH, "//p[normalize-space()='Family']")
    checked_box_for_topics= (By.XPATH, "//li[@id=':ri:-111111']//input[@type='checkbox']")
    Done_button = (By.XPATH, "//button[normalize-space()='Done']")
    country_dropdown = (By.XPATH, "//input[@id=':rj:']")
    select_country = (By.XPATH, "//li[@id=':rj:-option-0']")
    state_dropdown = (By.XPATH, "mui-component-select-province")
    select_state = (By.XPATH, "//li[contains(text(),'Farāh (AF-FRA)')]")
    city_text = (By.XPATH, "//input[@name='city']")
    zipcode_text = (By.XPATH, "//input[@name='addressZip']")
    street_address_text = (By.XPATH, "//input[@name='address1']")
    create_account_button = (By.XPATH, "//button[@id=':rl:']")




