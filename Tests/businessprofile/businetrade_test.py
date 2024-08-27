import time
from Pages.businessprofile.business_trade import businesstrade
from Pages.login_page import LoginPage
from config import Config
from Pages.userprofile.Registration.businessbasicSignupAPI import BusinessBasicSignup

def test_businesstrade(driver_setup):
    loginLog = BusinessBasicSignup()
    email, password = loginLog.signup()
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.login(email, password)
    businessTrade = businesstrade(driver)
    businessTrade.tradeInfo(driver)

