from selenium.webdriver.common.by import By
class loginLocators:
    email_textbox = (By.ID, 'loginForm_email')
    password_textbox = (By.ID,'loginForm_password')
    login_button = (By.XPATH,"//button[@type='submit']")
    login_error_message = (By.XPATH,"//div[@class='ant-form-item-explain-error']")