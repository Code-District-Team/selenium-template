import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver_setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Teardown after tests
    def teardown():
        driver.quit()
    request.addfinalizer(teardown)

    return driver
