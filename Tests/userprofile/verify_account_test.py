import time
from Pages.userprofile.verify_account import VerifyAccountPage
from config import Config
from Pages.userprofile.registration.test_individualSignupAPI import IndividualSignup
from Pages.login_page import LoginPage


def test_verifyAccount(driver_setup):
    # Signup with API method for new user
    apiSignup = IndividualSignup()
    # signup() method returns email and password
    email, password = apiSignup.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    verify_account = VerifyAccountPage(driver)
    verify_account.verify_account()
