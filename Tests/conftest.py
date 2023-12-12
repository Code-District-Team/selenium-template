import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver_setup(request):
    driver = webdriver.Chrome()  # Or any other browser initialization
    request.addfinalizer(driver.quit)
    return driver


