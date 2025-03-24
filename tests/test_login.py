from src.locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, PasswordRecoveryPageLocators
from src.utils import login, is_logged_in

EMAIL = "sergeifedoruk19999@ya.ru"
PASSWORD = "password"


def test_login_from_main_page(driver):
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
    is_logged_in(driver)


def test_login_from_account_button(driver):
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
    is_logged_in(driver)


def test_login_from_registration_page(driver):
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.GO_TO_REGISTRATION).click()
    driver.find_element(*RegistrationPageLocators.GO_TO_LOGIN_LINK).click()
    login(driver, EMAIL, PASSWORD)
    is_logged_in(driver)


def test_login_from_password_reset_page(driver):
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.GO_TO_PASSWORD_RESET).click()
    driver.find_element(*PasswordRecoveryPageLocators.GO_TO_LOGIN_LINK).click()
    login(driver, EMAIL, PASSWORD)
    is_logged_in(driver)
