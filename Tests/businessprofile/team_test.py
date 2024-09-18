import time
from config import Config
from Pages.businessprofile.team_page import teamPage
from Pages.userprofile.Registration.business_plus_registration import BusinessPlus
from Pages.businessprofile.businessinfo import Businessinfo

def test_team(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    businessPlus_signup = BusinessPlus(driver)
    team_page = teamPage(driver)
    businessPlus_signup.business_plus_signup(driver)
    time.sleep(1)
    businessinfo_instance = Businessinfo(driver)
    businessinfo_instance.skip_account_verification()
    businessinfo_instance.skip_account_verification()
    team_page.team_internal_members_invite()
    team_page.team_external_members()