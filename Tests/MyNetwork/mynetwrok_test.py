import time
import pytest
from Pages.MyNetwork.signup_pytest_function import MyNetwork
from Pages.login_page import LoginPage
from config import Config
from Pages.businessprofile.businessinfo import Businessinfo
from Pages.MyNetwork.mynetwork import NetworkPage

@pytest.fixture(scope="module")
def create_user():
    my_network = MyNetwork()
    my_network.signup()
    return my_network

@pytest.fixture(scope="module")
def driver_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture(scope="module")
def login_page(driver_setup):
    driver = driver_setup
    driver.get(Config.base_url)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(MyNetwork.email1, MyNetwork.password1)
    return login_page

def test_signup(create_user):
    # Verify that user creation was successful
    assert MyNetwork.email1 is not None
    assert MyNetwork.password1 is not None
    assert MyNetwork.userId1 is not None
    assert MyNetwork.email2 is not None
    assert MyNetwork.password2 is not None
    assert MyNetwork.userId2 is not None

@pytest.fixture(scope="module")
def skip_account_verification_fixture(driver_setup):
    return Businessinfo(driver_setup)

def test_skip_account_verification(skip_account_verification_fixture):
    skip_account_verification_fixture.skip_account_verification()

@pytest.fixture(scope="module")
def navigate_to_user_two_profile(driver_setup):
    def open_and_close_new_window():
        driver = driver_setup
        original_window = driver.current_window_handle
        url = f"https://development.d2vtpkgl21lrum.amplifyapp.com/p/{MyNetwork.userId2}"
        driver.execute_script(f"window.open('{url}');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)  # Wait for the new page to load
        test_skip_account_verification(Businessinfo(driver))
        time.sleep(10)
        test_follow_sendcard(NetworkPage(driver))
        time.sleep(10)

        # Close the new window
        driver.close()

        # Switch back to the original window
        driver.switch_to.window(original_window)

    return open_and_close_new_window

@pytest.fixture(scope="module")
def follow_sendcard_fixture(driver_setup):
    return NetworkPage(driver_setup)

def test_follow_sendcard(follow_sendcard_fixture):
    follow_sendcard_fixture.follow_send_business_card()
    follow_sendcard_fixture.send_business_card()

def test_userA_Network_tab(follow_sendcard_fixture):
    follow_sendcard_fixture.network_Tab_for_UserA()
def test_bloclock_unblock(follow_sendcard_fixture):
    follow_sendcard_fixture.block_business_card_request()
@pytest.fixture(scope="module")
def login_user_b_fixture(driver_setup):
    driver = driver_setup
    login_page_b = LoginPage(driver)
    return login_page_b

def login_user_b(login_user_b_fixture):
    login_user_b_fixture.login(MyNetwork.email2, MyNetwork.password2)
def test_userB_Network_tab(follow_sendcard_fixture):
    follow_sendcard_fixture.network_Tab_for_UserB()


def test_mynetwork(create_user, skip_account_verification_fixture, login_page, navigate_to_user_two_profile, follow_sendcard_fixture, login_user_b_fixture):
    test_signup(create_user)
    time.sleep(10)
    test_skip_account_verification(skip_account_verification_fixture)
    time.sleep(10)
    navigate_to_user_two_profile()
    time.sleep(5)
    test_userA_Network_tab(follow_sendcard_fixture)
    time.sleep(5)
    login_user_b(login_user_b_fixture)
    time.sleep(10)
    test_skip_account_verification(skip_account_verification_fixture)
    time.sleep(10)
    test_userB_Network_tab(follow_sendcard_fixture)
def test_block_unblock(create_user, skip_account_verification_fixture, login_page, navigate_to_user_two_profile, follow_sendcard_fixture, login_user_b_fixture):
    test_signup(create_user)
    time.sleep(10)
    test_skip_account_verification(skip_account_verification_fixture)
    time.sleep(10)
    navigate_to_user_two_profile()
    time.sleep(5)
    test_userA_Network_tab(follow_sendcard_fixture)
    time.sleep(5)
    login_user_b(login_user_b_fixture)
    time.sleep(10)
    test_skip_account_verification(skip_account_verification_fixture)
    time.sleep(10)
    test_bloclock_unblock(follow_sendcard_fixture)




