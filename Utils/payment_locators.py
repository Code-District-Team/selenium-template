from selenium.webdriver.common.by import By
class payment_page_locators:
    card_number_input_field = (By.XPATH, '//*[@id="braintree-hosted-field-number"]')

    expires_input_field = (By.ID, "expiration")
    security_code_input_field = (By.ID, "cvv")
    continue_button = (By.ID, ":ro:")
