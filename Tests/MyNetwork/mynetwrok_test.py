# import time
# import pytest
# from Pages.MyNetwork.signup_pytest_function import MyNetwork
# from Pages.login_page import LoginPage
# from Tests.MyNetwork.test_blockunblock import signup
# from config import Config
# from Pages.businessprofile.businessinfo import Businessinfo
# from Pages.MyNetwork.mynetwork import NetworkPage
#
#
# @pytest.fixture(scope="module")
# def create_user():
#     """Sign up users before the test."""
#     my_network = MyNetwork()
#     my_network.signup()  # Creates User A and User B accounts
#     return my_network
#
#
# @pytest.fixture(scope="module")
# def login_user_a(driver_setup):
#     """Login User A."""
#     driver = driver_setup
#     driver.get(Config.base_url)
#     driver.maximize_window()
#     login_page = LoginPage(driver)
#     login_page.login(MyNetwork.email1, MyNetwork.password1)  # Login with User A
#     return login_page
#
#
# @pytest.fixture(scope="module")
# def login_user_b(driver_setup):
#     """Create a new WebDriver session for User B and log them in."""
#     driver = driver_setup
#     driver.get(Config.base_url)  # Load base URL for User B login
#     login_page_b = LoginPage(driver)
#     return login_page_b
#
#
# @pytest.fixture(scope="module")
# def skip_account_verification_fixture(driver_setup):
#     """Fixture to skip account verification."""
#     return Businessinfo(driver_setup)
#
#
# def skip_account_verification(skip_account_verification_fixture):
#     """Method to skip account verification."""
#     skip_account_verification_fixture.skip_account_verification()
#
#
# @pytest.fixture(scope="module")
# def follow_sendcard_fixture(driver_setup):
#     """Fixture to handle network actions for both User A and B."""
#     return NetworkPage(driver_setup)
#
#
# def follow_sendcard(follow_sendcard_fixture):
#     """Follow and send business cards."""
#     follow_sendcard_fixture.follow_send_business_card()
#     follow_sendcard_fixture.send_business_card()
#
#
# def userA_Network_tab(follow_sendcard_fixture):
#     """Access the network tab for User A."""
#     follow_sendcard_fixture.network_Tab_for_UserA()
#
#
# def userB_Network_tab(follow_sendcard_fixture):
#     """Access the network tab for User B."""
#     follow_sendcard_fixture.network_Tab_for_UserB()
#
#
# @pytest.fixture(scope="module")
# def navigate_to_user_two_profile(driver_setup):
#     """Navigate to User Two's profile and perform actions."""
#
#     def open_and_close_new_window():
#         driver = driver_setup
#         original_window = driver.current_window_handle
#         url = f"https://development.d2vtpkgl21lrum.amplifyapp.com/p/{MyNetwork.userId2}"
#
#         # Open new window for User Two
#         driver.execute_script(f"window.open('{url}');")
#         driver.switch_to.window(driver.window_handles[-1])
#         time.sleep(5)  # Wait for page load
#
#         # Skip account verification
#         skip_account_verification(Businessinfo(driver))
#         time.sleep(5)
#
#         # Perform follow and send card actions
#         follow_sendcard(NetworkPage(driver))
#         time.sleep(5)
#
#         # Close new window and return to the original one
#         driver.close()
#         driver.switch_to.window(original_window)
#
#     return open_and_close_new_window
#
#
# def test_mynetwork(create_user, skip_account_verification_fixture, login_user_a, navigate_to_user_two_profile,
#                    follow_sendcard_fixture, login_user_b):
#     """Test full flow of both users interacting with My Network."""
#
#     # Step 1: User A signup and validation
#     signup(create_user)
#     time.sleep(3)
#
#     # Step 2: User A skips account verification
#     skip_account_verification(skip_account_verification_fixture)
#     time.sleep(3)
#
#     # Step 3: User A navigates to User Two's profile and sends a business card
#     navigate_to_user_two_profile()
#     time.sleep(3)
#
#     # Step 4: User A interacts with network tab
#     userA_Network_tab(follow_sendcard_fixture)
#     time.sleep(3)
#
#     # Step 5: User A session completes; Clear cookies to avoid session conflicts
#     login_user_a.driver.delete_all_cookies()
#
#     # Step 6: User B logs in
#     login_user_b.login(MyNetwork.email2, MyNetwork.password2)  # Login with User B
#     time.sleep(3)
#
#     # Step 7: User B skips account verification
#     skip_account_verification(skip_account_verification_fixture)
#     time.sleep(3)
#
#     # Step 8: User B interacts with network tab
#     userB_Network_tab(follow_sendcard_fixture)
