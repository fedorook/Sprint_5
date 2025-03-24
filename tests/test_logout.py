from src.utils import login
from src.locators import MainPageLocators, ProfilePageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "sergeifedoruk19999@ya.ru"
PASSWORD = "password"


def test_logout_from_profile(driver):
    # Log in first
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    login(driver, EMAIL, PASSWORD)

    # Open profile (Личный Кабинет)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Click "Выход"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
    ).click()

    # Ensure we’re back on the login page (email field is visible)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
