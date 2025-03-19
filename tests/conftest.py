import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Driver initialisation
    driver = webdriver.Chrome()
    # Returning the driver to a test
    yield driver
    # Closing the browser
    driver.quit()
