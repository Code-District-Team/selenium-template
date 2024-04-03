from config import Config
from Pages.login_page import LoginPage
from Resources.loginData import loginTestData
from Pages.account_management.subscription_upgrade_individual_to_freelance import Subscription_upgrade_individual_to_freelance
from Pages.account_management.password_change import password_change
import time


def test_indvidual_to_freelance_upgrade(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.login(loginTestData.valid_credential["validEmail"], loginTestData.valid_credential["password"])
    skip_account_verification = password_change(driver)
    skip_account_verification.skip_account_verification()
    upgrade_individual_to_freelance = Subscription_upgrade_individual_to_freelance(driver)
    upgrade_individual_to_freelance.upgrade_subcription_indvidual_to_free_lance()
    subscription_payment = Subscription_upgrade_individual_to_freelance(driver)
    subscription_payment.payment_for_subscription_upgrade(driver)
    time.sleep(20)