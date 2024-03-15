from selenium.webdriver.common.by import By
class loginLocators:
    email_textbox = (By.XPATH, "(//input[@placeholder='Enter Your Email'])[1]")
    password_textbox = (By.XPATH,"(//input[@placeholder='••••••••••••••••••'])[1]")
    login_button = (By.ID,":r0:")
    empty_email_field_error = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/div[1]/p[1]")
    empty_password_field_error = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/div[2]/p[1]")
    status_message = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]")