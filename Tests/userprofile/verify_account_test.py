import time
from Pages.userprofile.verify_account import VerifyAccountPage
from config import Config
from Pages.userprofile.Registration.individualSignupAPI import IndividualSignup
from Pages.login_page import LoginPage
from Pages.businessprofile.businessinfo import Businessinfo


def test_verifyAccount(driver_setup):
    # Signup with API method for new user
    apiSignup = IndividualSignup()
    # signup() method returns email and password
    email, password = apiSignup.test_signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    businessinfo_instance = Businessinfo(driver_setup)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()

    verify_account = VerifyAccountPage(driver)
    verify_account.verify_account()
