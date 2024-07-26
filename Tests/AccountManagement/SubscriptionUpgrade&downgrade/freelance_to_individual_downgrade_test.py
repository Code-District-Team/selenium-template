from config import Config
from Pages.userprofile.account_management.subscription_downgrade_freelance_individual import \
    Subscription_downgrade_freelance_to_individual
import time
from Pages.userprofile.Registration.freerlance_registration_page import FreelanceRegistration
from Pages.businessprofile.businessinfo import Businessinfo


def test_freelance_to_individual_downgrade(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()

    freelance_signup = FreelanceRegistration(driver)
    freelance_signup.signup_freelance(driver)

    skip_account_verification = Businessinfo(driver)
    skip_account_verification.skip_account_verification()

    subscription_downgrade = Subscription_downgrade_freelance_to_individual(driver)
    subscription_downgrade.downgrade_to_individual()

    time.sleep(10)
