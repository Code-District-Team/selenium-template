
import time
from Pages.userprofile.user_follow_unfollw import User_follow_unfollow
from config import Config
from Pages.businessprofile.businessinfo import Businessinfo

from Pages.userprofile.Registration.businessbasic_registration import BusinessBasicRegistration
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
def test_follow_unfollow(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
    businessinfo_instance = Businessinfo(driver_setup)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()
    driver_setup.get("https://development.d2vtpkgl21lrum.amplifyapp.com/p/asad-hafeez-9cec9")
    time.sleep(5)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()
    follow_unfollow = User_follow_unfollow(driver_setup)
    follow_unfollow.test_userprofile()