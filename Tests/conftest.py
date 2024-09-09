import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver_setup(request):
   options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver
