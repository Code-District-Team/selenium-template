from selenium.webdriver.common.by import By
class loginLocators:
    email_textbox = (By.ID, "login-email")
    password_textbox = (By.ID, "password-input")
    login_button = (By.ID,":r0:")
    empty_email_field_error = (By.XPATH, "//p[normalize-space()='Please enter your email.']")
    empty_password_field_error = (By.XPATH, "//p[normalize-space()='Please enter password']")
    status_message = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]")