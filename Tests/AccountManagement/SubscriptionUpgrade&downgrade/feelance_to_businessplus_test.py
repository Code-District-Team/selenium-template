from config import Config
from Pages.userprofile.account_management.subscription_upgrade_freelance_to_businessplus import Subscription_upgrade_freelance_to_businessplus

import time
from Pages.userprofile.Registration.freerlance_registration_page import FreelanceRegistration
from Pages.businessprofile.businessinfo import Businessinfo


def test_freelance_to_businessplus_upgrade(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()

    freelance_signup = FreelanceRegistration(driver)
    freelance_signup.signup_freelance(driver)

    skip_account_verification = Businessinfo(driver)
    skip_account_verification.skip_account_verification()

    subscription_upgrade = Subscription_upgrade_freelance_to_businessplus(driver)
    subscription_upgrade.freelance_to_businessplus(driver)

    time.sleep(10)