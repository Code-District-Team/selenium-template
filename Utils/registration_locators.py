from selenium.webdriver.common.by import By
class registrationLocators:
    signup_button = (By.XPATH, "(//a[normalize-space()='Sign Up']")
    Continue_button = (By.XPATH,"(//button[normalize-space()='Continue']")
    email_text = (By.XPATH,"//input[@name='username']")
    continue_2_button = (By.XPATH,"//button[@id=':r3:']")
    checkbox_1 = (By.XPATH, "//input[@name='opsNotificationConsent']")
    name_text = (By.XPATH, "//input[@name='firstName']")
    surname_text = (By.XPATH, "//input[@name='lastName']")
    newPassword_text = (By.XPATH, "//input[@name='password']")
    repeatPassword_text = (By.XPATH, "//input[@name='confirmPassword']")