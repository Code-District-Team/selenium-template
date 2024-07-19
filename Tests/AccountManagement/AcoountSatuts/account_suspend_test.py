import time

from Pages.login_page import LoginPage
from Pages.userprofile.registration.test_individualSignupAPI import IndividualSignup
from Pages.userprofile.account_management.account_status import AccountStatus
from Resources.loginData import loginTestData
from config import Config
from Pages.businessprofile.businessinfo import Businessinfo


def test_account_suspend_activation(driver_setup):
    new_user = IndividualSignup()
    username, password = new_user.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(username,password)
    skipAccountVerification = Businessinfo(driver_setup)
    skipAccountVerification.skip_account_verification()

    account_suspend = AccountStatus(driver)
    account_suspend.test_account_suspend_and_activation()
