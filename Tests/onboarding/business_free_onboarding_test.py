# from Pages.businessprofile.businessinfo import Businessinfo
# from Pages.userprofile.Registration.businessbasicSignupAPI import BusinessBasicSignup
# from Pages.userprofile.onboarding.onboarding_page import OnboardingPage
# from config import Config
# from Pages.login_page import LoginPage
#
#
# def test_business_free_onboarding(driver_setup):
#     loginLog = BusinessBasicSignup()
#     email, password = loginLog.signup()
#     driver = driver_setup
#     driver.get(Config.base_url)
#     driver.maximize_window()
#     loginPage = LoginPage(driver_setup)
#     loginPage.login(email, password)
#     skipAccountVerification = Businessinfo(driver)
#     skipAccountVerification.skip_account_verification()
#
#     business_free_onboarding = OnboardingPage(driver)
#     business_free_onboarding.onboarding_start()
