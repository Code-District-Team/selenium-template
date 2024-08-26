from selenium.webdriver.common.by import By


class account_status_locators:
    account_status_tab = (By.XPATH, "(//button[normalize-space()='Account Status'])[1]")
    suspend_account_button = (By.ID, 'active')
    active_account_button = (By.ID, "suspend")
    delete_account_button = (By.XPATH, "//button[normalize-space()='Delete my account and all data']")
    confirm_suspend_account_button = (By.ID, "suspendModalButton")
    confirm_active_account_button = (By.ID, "activateModalButton")
    confirm_delete_account_button = (By.ID, "deleteModalButton")
    account_status = (By.XPATH, '//div[@role=\'status\']')