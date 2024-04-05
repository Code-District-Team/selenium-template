from selenium.webdriver.common.by import By


class account_status_locators:
    account_status_tab = (By.XPATH, '//button[normalize-space()=\'Account Status\']')
    suspend_account_button = (By.XPATH, '//button[normalize-space()=\'Suspend my account\']')
    delete_account_button = (By.XPATH, "//button[normalize-space()='Delete my account and all data']")
    confirm_suspend_account_button = (By.ID, ":ra:")
    active_my_account_button = (By.XPATH, "(//body)[1]")
    confirm_active_account_button = (By.ID, ":rl:")
    confirm_delete_account_button = (By.ID, ":ra:")
    account_status = (By.XPATH, '//div[@role=\'status\']')