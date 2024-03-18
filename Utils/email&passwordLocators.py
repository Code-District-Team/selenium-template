from selenium.webdriver.common.by import By
class email&passwordlocators:
    skip_onboarding = (By.XPATH, "//button[normalize-space()='Skip']")
    emai_tab = (By.XPATH, "(//button[normalize-space()='Email & Password'])[1]")
    change_email_button = (By.XPATH, "(// button[normalize-space() = 'Change'])[1]")
    new_email_field = (By.XPATH, "//input[@placeholder='New Email']")
    retype_email_field = (By.XPATH, "(//input[@placeholder='Repeat New Email'])[1]")
    verify_button = (By.ID, ":r7:")
    cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")