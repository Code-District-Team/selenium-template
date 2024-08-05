from selenium.webdriver.support.ui import WebDriverWait
import time
from faker import Faker
from selenium.webdriver.common.by import By
from Utils.verify_account_locators import VerifyAccountLocator
from selenium.webdriver.support import expected_conditions as EC
faker = Faker()
class VerifyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.email1 = faker.email()
        self.email2 = faker.email()
        self.email3 = faker.email()

    def click_profile_avatar(self):
        close_button = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.close))
        time.sleep(1)
        close_button.click()
        time.sleep(2)
        profile_click = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.profileAvatar))
        profile_click.click()

    def click_verify_account(self):
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.verifyAccount)).click()

    def click_inviteReviewer(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.inviteReviewer)).click()

    def click_searchBar(self):
       serchBar = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.searchBar))
       serchBar.clear()
       serchBar.click()
       time.sleep(2)
       serchBar.send_keys("david")

    def invite_user(self):
        invite_by_email = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.inviteByEmail))
        invite_by_email.click()
        time.sleep(1)

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.emailBox)).send_keys(self.email1)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.addButton)).click()
        time.sleep(2)

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.emailBox)).clear()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.emailBox)).send_keys(self.email2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.addButton)).click()
        time.sleep(2)

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.emailBox)).send_keys(self.email3)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.addButton)).click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(VerifyAccountLocator.message)).send_keys(faker.paragraph())

    def click_selected_invitee(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(VerifyAccountLocator.selectedInvitee)).click()

    def review_status(self):
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(VerifyAccountLocator.reviewStatus)).click()
    def assert_listing(self):
        user1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"(// h4[text() = '{self.email1}'])[1]")))
        time.sleep(1)
        user1email = user1.text
        print(user1email)
        user2 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"(// h4[text() = '{self.email2}'])[1]")))
        user2email = user2.text
        print(user2email)
        user3 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"(// h4[text() = '{self.email3}'])[1]")))
        user3email = user3.text
        print(user3email)
        assert user1email == self.email1
        assert user2email == self.email2
        assert user3email == self.email3
        time.sleep(1)

    def resend_button(self):
        user1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(VerifyAccountLocator.resendButton))
        user1.click()
        success_message_element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(VerifyAccountLocator.success_message))
        # Get the text content of the element
        actual_message = success_message_element.text
        print(actual_message)
        # Expected success message
        expected_message = "1 Invitation(s) sent successfully."
        # Assert that the actual message matches the expected message
        assert actual_message == expected_message

    def verify_account(self):
        self.click_profile_avatar()
        self.click_verify_account()
        self.click_inviteReviewer()
        self.click_searchBar()
        self.invite_user()
        self.click_selected_invitee()
        self.review_status()
        self.assert_listing()
        time.sleep(2)
        self.resend_button()