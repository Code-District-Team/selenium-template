
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC



class loginLocators:
    loginPage = (By.ID, "btnLogin")
    email_textbox = (By.ID, "login-email")
    password_textbox = (By.ID, "password-input")
    login_button = (By.XPATH, "(//button[normalize-space()='Log In'])[1]")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_login_page(self):
        loginPage= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located( loginLocators.loginPage))
        loginPage.click()

    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located( loginLocators.email_textbox))
        email_field.send_keys(email)


    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loginLocators.password_textbox))
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loginLocators.login_button))
        login_button.click()






    def login(self, email, password):
        self.navigate_to_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()


