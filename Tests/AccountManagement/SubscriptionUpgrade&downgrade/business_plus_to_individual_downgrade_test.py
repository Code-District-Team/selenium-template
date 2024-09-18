from config import Config
from Pages.userprofile.account_management.subscription_downgrade_business_plus_to_individual import Subscription_downgrade_business_plus_to_individual
import time
from Pages.userprofile.Registration.business_plus_registration import BusinessPlus
from Pages.businessprofile.businessinfo import Businessinfo


def test_business_plus_to_individual_downgrade(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()

    businessPlus = BusinessPlus(driver)
    businessPlus.business_plus_signup(driver)

    skip_account_verification = Businessinfo(driver)
    skip_account_verification.skip_account_verification()
    skip_account_verification.skip_account_verification()

    subscription_downgrade = Subscription_downgrade_business_plus_to_individual(driver)
    subscription_downgrade.subscription_downgrade_business_plus_to_individual(driver)

    time.sleep(3)
