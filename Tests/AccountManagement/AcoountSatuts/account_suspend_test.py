
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.login_page import LoginPage
from Pages.userprofile.Registration.individualSignupAPI import IndividualSignup
from Pages.userprofile.account_management.account_status import AccountStatus
from Utils.profile_locators import profileLocators
from config import Config
from Pages.businessprofile.businessinfo import Businessinfo



def test_account_suspend_activation(driver_setup):
    new_user = IndividualSignup()
    username, password = new_user.test_signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    login_page = LoginPage(driver)

    login_page.login(username, password)
    skipAccountVerification = Businessinfo(driver_setup)
    skipAccountVerification.skip_account_verification()
    skipAccountVerification.skip_account_verification()

    account_suspend = AccountStatus(driver)
    account_suspend.test_account_suspend_and_activation()
    account_suspend.test_account_delete()
    login_page.login(username, password)
    loginToast_alert = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(profileLocators.businessAlert))
    actual_loginToast_text = loginToast_alert.text
    expected_loginToast_text = "Incorrect username or password."
    assert actual_loginToast_text == expected_loginToast_text, f"Expected '{expected_loginToast_text}', but got '{actual_loginToast_text}'"
