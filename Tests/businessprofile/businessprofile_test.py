import time

from Pages.login_page import LoginPage
from Pages.userprofile.Registration.businessbasicSignupAPI import BusinessBasicSignup
from Pages.businessprofile.businessinfo import Businessinfo
from config import Config


def test_businessinfo(driver_setup):
    loginLog = BusinessBasicSignup()
    email, password = loginLog.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver_setup)
    loginPage.login(email, password)
    businessinfo_instance = Businessinfo(driver_setup)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.changeBusinessInfo()






