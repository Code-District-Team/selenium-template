from selenium.webdriver.common.by import By


class email_password_locators:
    skip_onboarding = (By.ID, "btn-skip")
    emai_tab = (By.XPATH, "(//button[normalize-space()='Email & Password'])[1]")
    change_email_button = (By.ID, "change-email")
    new_email_field = (By.ID, "new-email")
    retype_email_field = (By.ID, "repeat-new-email")
    cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    change_password_button = (By.ID, "change-password")
    old_password_field = (By.ID, "old-password")
    new_password_field = (By.NAME, "new-password")
    repeat_password_filed = (By.NAME, "repeat-newpassword")
    save_button = (By.ID, "btn-save")

