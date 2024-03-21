import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuerrillaMailPage:
    EMAIL_WIDGET = (By.ID, "email-widget")

    def __init__(self, driver):
        self.driver = driver

    def get_email_address(self):
        # Get unique email address from gurellia domain service.
        email_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL_WIDGET))
        return email_element.text






class EmailInboxPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_email_list(self):
        # Wait for the email list to appear
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "email_list")))

    def click_verification_email(self):
        # Click on the verification email.

        verification_email = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "(//td[normalize-space()='no-reply@verificationemail.com'])[1]")))
        self.driver.execute_script("window.scrollBy(0, window.innerHeight/2);")

        verification_email.click()
        time.sleep(4)


    def copy_otp(self):
        self.driver.execute_script("window.scrollBy(0, window.innerHeight/4);")
        copy_otp = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/h3[1]")))
        text = copy_otp.text
        return text