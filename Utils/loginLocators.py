from selenium.webdriver.common.by import By
class loginLocators:
    email_textbox = (By.XPATH, "(//input[@placeholder='Enter Your Email'])[1]")
    password_textbox = (By.XPATH,"(//input[@placeholder='••••••••••••••••••'])[1]")
    login_button = (By.ID,":r0:")