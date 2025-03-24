import pytest
from selenium import webdriver
from src.config import Config

@pytest.fixture
def driver():
    # Driver initialisation
    driver = webdriver.Chrome()
    # Landing on the base URL
    driver.get(Config.URL)
    # Returning the driver to a test
    yield driver
    # Closing the browser
    driver.quit()
