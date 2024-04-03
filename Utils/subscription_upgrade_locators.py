from selenium.webdriver.common.by import By
class Subscriptionupgradelocators:

    subscription_tab = (By.XPATH, '//button[normalize-space()=\'Subscription\']')
    upgrade_to_freelance_button = (By.XPATH, '//button[normalize-space()=\'Upgrade to Freelancer\']')
    description_text_box = (By.ID, ":rg:")
    hourly_rate = (By.NAME, "hourlyRate")
    currency_dropdown_field = (By.XPATH, "//div[@id='mui-component-select-currency']")
    currency_dropdown_option = (By.XPATH, "//li[contains(text(),'Costa Rica Colon (₡)')]")
    minimum_project_size = (By.NAME, "minProjectSize")
    availability_dropdown = (By.ID, "mui-component-select-availability")
    availability_dropdown_option = (By.XPATH, "//li[normalize-space()='Full-Time']")
    continue_button = (By.XPATH, "//button[normalize-space()='Continue']")
    chose_a_country_input = (By.ID, ":r1e:")
    state_field_dropdown = (By.ID, "mui-component-select-province")
    state_input_field_option = (By.XPATH, "//li[contains(text(),'Badakhshān (AF-BDS)')]")
    upgrade_subscription_button = (By.ID, ":r11:")
    upgrade_to_business_basic = (By.XPATH, "//button[normalize-space()='Upgrade to Business Basic']")
    upgrade_to_business_plus = (By.XPATH, "//button[normalize-space()='Upgrade to Business Plus']")
    seat_increase_button = (By.XPATH, "//div[@role='presentation']//button[2]//*[name()='svg']")


