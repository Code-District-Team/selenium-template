from Pages.login_page import LoginPage
from Pages.userprofile.Registration.individualSignupAPI import IndividualSignup
from config import Config
from Pages.businessprofile.businessinfo import Businessinfo
from Pages.userprofile.user_resume_tab import User_resume



def test_resume(driver_setup):
    loginLog = IndividualSignup()
    email, password = loginLog.test_signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    businessinfo_instance = Businessinfo(driver_setup)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()
    userResume = User_resume(driver_setup)
    userResume.test_resume(driver_setup)