import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="module")
def driver_setup(request):
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    request.addfinalizer(driver.quit)
    return driver
