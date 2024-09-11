import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver_setup(request):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")  # Required for some CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues on CI

    # Initialize the WebDriver with Chrome options
    driver = webdriver.Chrome(options=chrome_options)

    # Add a finalizer to quit the driver after the tests are done
    request.addfinalizer(driver.quit)
    
    return driver
