from src.utils import login
from src.locators import MainPageLocators, ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import ConstructorSectionLocators


def test_go_to_profile_from_main(driver):
    driver.get(Config.LOGIN_URL)
    login(driver, "sergeifedoruk19999@ya.ru", "password")

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Expect logout button on profile page
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
    )


def test_go_to_constructor_from_profile(driver):
    driver.get(Config.LOGIN_URL)
    login(driver, "sergeifedoruk19999@ya.ru", "password")

    # Go to profile first
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
    )

    # Now go back to constructor via "Конструктор" link
    driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorSectionLocators.BUNS_TAB)
    )


def test_go_to_constructor_from_logo(driver):
    driver.get(Config.LOGIN_URL)
    login(driver, "sergeifedoruk19999@ya.ru", "password")

    # Go to profile first
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
    )

    # Click logo to go back to constructor
    driver.find_element(*ProfilePageLocators.LOGO_LINK).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorSectionLocators.BUNS_TAB)
    )
