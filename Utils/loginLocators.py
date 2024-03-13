from selenium.webdriver.common.by import By
class loginLocators:
    email_textbox = (By.XPATH, "(//input[@placeholder='Enter Your Email'])[1]")
    password_textbox = (By.XPATH,"(//input[@placeholder='••••••••••••••••••'])[1]")
    login_button = (By.ID,":r0:")
    empty_email_field_error = (By.CSS_SELECTOR,"body > div:nth-child(21) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > p:nth-child(3)")
    empty_password_field_error = (By.XPATH, "//p[normalize-space()='Please enter password']")