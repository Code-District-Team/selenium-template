import selenium.webdriver.common.by


class loginLocators:
    loginPage = (selenium.webdriver.common.by.By.ID, "btnLogin")
    email_textbox = (selenium.webdriver.common.by.By.ID, "login-email")
    password_textbox = (selenium.webdriver.common.by.By.ID, "password-input")
    login_button = (selenium.webdriver.common.by.By.XPATH, "(//button[normalize-space()='Log In'])[1]")
    empty_email_field_error = (selenium.webdriver.common.by.By.XPATH, "//p[normalize-space()='Please enter your email.']")
    empty_password_field_error = (selenium.webdriver.common.by.By.XPATH, "//p[normalize-space()='Please enter password']")
    status_message = (selenium.webdriver.common.by.By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]")

