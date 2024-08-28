import time

from Pages.login_page import LoginPage
# from config import Config
# from Pages.businessprofile.businessinfo import Businessinfo
# from Pages.userprofile.user_resume_tab import User_resume
# from Resources.loginData import loginTestData
#
#
# def test_resume(driver_setup):
#     driver = driver_setup
#     driver.get(Config.base_url)
#     driver.maximize_window()
#     login_page = LoginPage(driver)
#     login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
#     businessinfo_instance = Businessinfo(driver_setup)
#     businessinfo_instance.skip_account_verification()
#     businessinfo_instance.skip_account_verification()
#     time.sleep(10)
#     userResume = User_resume(driver_setup)
#     userResume.test_resume(driver_setup)