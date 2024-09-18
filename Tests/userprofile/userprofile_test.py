


from Pages.businessprofile.businessinfo import Businessinfo
from Pages.userprofile.user_profile import Userprofile
from Pages.login_page import LoginPage
from config import Config
from Pages.userprofile.Registration.individualSignupAPI import IndividualSignup

def test_userprofile(driver_setup):
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
    userProfile = Userprofile(driver_setup)
    userProfile.user_profile()