
from Pages.userprofile.Registration.individualSignupAPI import IndividualSignup
from config import Config
from Pages.login_page import LoginPage
from Pages.userprofile.account_management.password_change import password_change
from Pages.businessprofile.businessinfo import Businessinfo


def test_change_password(driver_setup):
    loginLog = IndividualSignup()
    email, password = loginLog.test_signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    skipAccountVerification = Businessinfo(driver)
    skipAccountVerification.skip_account_verification()
    skipAccountVerification.skip_account_verification()
    change_password = password_change(driver)
    change_password.change_password(password)



