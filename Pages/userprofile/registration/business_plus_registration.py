from selenium.webdriver.support.ui import WebDriverWait
import time
from Pages.userprofile.registration.payment_page import payment_processing
from Utils.registration_locators import registrationLocators
from Pages.userprofile.registration.businessbasic_registration import business_basic_registration
from selenium.webdriver.support import expected_conditions as EC
from Pages.userprofile.registration.Individual_registration_page import RegistrationPage
from config import Config
class BusinessPluss:

    def __init__(self, driver):
        self.driver = driver



    def select_business_account(self):
        business_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(registrationLocators.business_plus_account))
        business_button.click()

    def add_seats(self):
        add_seats = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(registrationLocators.seats_button))
        add_seats.click()
        add_seats.click()
    def business_plus_registration(self, email_address,driver):
        registration_page_instance = RegistrationPage(driver)
        business_registration_instance = business_basic_registration(driver)
        payment_screen = payment_processing(driver)


        original_window_handle = self.driver.current_window_handle
        self.driver.execute_script("window.open('" + Config.base_url + "', 'new window')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        registration_page_instance.click_signup_button()
        self.select_business_account()
        registration_page_instance.click_continue_button()
        business_registration_instance.add_business()
        registration_page_instance.click_continue_button()
        registration_page_instance.enter_email(email_address)
        business_registration_instance.click_checkbox()
        registration_page_instance.click_continue_button()
        business_registration_instance.personal_info()
        registration_page_instance.click_continue_button()
        business_registration_instance.job_title()
        registration_page_instance.click_continue_button()
        registration_page_instance.select_topic()
        registration_page_instance.click_continue_button()
        registration_page_instance.select_address()
        registration_page_instance.create_account_button()

        self.add_seats()
        time.sleep(3)
        registration_page_instance.click_continue_button()
        self.driver.switch_to.window(original_window_handle)
        time.sleep(3)
        self.driver.refresh()


    def business_plus_payment(self, driver):
        payment_screen = payment_processing(driver)

        payment_screen.payment_processing()
        time.sleep(20)





