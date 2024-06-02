# follow&unfollow_test.py
import time
from Pages.userprofile.user_follow_unfollw import User_follow_unfollow
from Pages.businessprofile.businessinfo import Businessinfo
from Pages.userprofile.user_profile import Userprofile
from Tests.registration.basic_business_registration_test import test_business_basic


def testfollow_unfollow(driver_setup):
    # Perform the basic business registration test
    signup = test_business_basic(driver_setup)

    # Adding a delay to simulate waiting for some process to complete
    time.sleep(5)

    # URL to open in a new window
    new_window_url = 'https://development.d2vtpkgl21lrum.amplifyapp.com/p/asad-hafeez-9cec9'

    # Open a new window with the specified URL
    driver_setup.execute_script(f"window.open('{new_window_url}', '_blank');")

    # Switch to the new window
    driver_setup.switch_to.window(driver_setup.window_handles[-1])

    # Here you can perform any actions needed in the new window

    # Optionally print the title of the new window
    print(driver_setup.title)

    # Close the new window
    driver_setup.close()

    # Switch back to the original window
    driver_setup.switch_to.window(driver_setup.window_handles[0])
