import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver_setup(request):
    ChromeOptions options = new ChromeOptions();
    options.addArguments("--headless")
    request.addfinalizer(driver.quit)
    return driver
