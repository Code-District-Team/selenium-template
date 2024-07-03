import time
from config import Config
from Pages.businessprofile.businessinfo import Businessinfo
from Pages.businessprofile.byerintent import buyerintent
from Resources.loginData import loginTestData
from Pages.login_page import LoginPage


def test_buyer_intent(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
    businessinfo_instance = Businessinfo(driver_setup)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()
    time.sleep(10)
    buyerIntent = buyerintent(driver_setup)
    buyerIntent.buyer_intent()

