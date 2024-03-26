from selenium.webdriver.common.by import By


class email_password_locators:
    skip_onboarding = (By.XPATH, "//button[normalize-space()='Skip']")
    emai_tab = (By.XPATH, "(//button[normalize-space()='Email & Password'])[1]")
    change_email_button = (By.XPATH, "(// button[normalize-space() = 'Change'])[1]")
    new_email_field = (By.XPATH, "//input[@placeholder='New Email']")
    retype_email_field = (By.XPATH, "(//input[@placeholder='Repeat New Email'])[1]")
    cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    change_password_button = (By.XPATH, "//button[normalize-space()='Change Password']")
    old_password_field = (By.NAME, "oldPassword")
    new_password_field = (By.NAME, "newPassword")
    repeat_password_filed = (By.NAME, "repeatNewPassword")
    save_password_button = (By.XPATH, '//*[@id=":r9:"]')

