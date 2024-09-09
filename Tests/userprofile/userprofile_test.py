import time


from Pages.businessprofile.businessinfo import Businessinfo
from Pages.userprofile.user_profile import Userprofile
from Pages.login_page import LoginPage
from config import Config
from Resources.loginData import loginTestData

def test_userprofile(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
    businessinfo_instance = Businessinfo(driver_setup)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()
    time.sleep(10)
    userProfile = Userprofile(driver_setup)
    userProfile.user_profile()