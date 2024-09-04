import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver_setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless=chrome")
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver
