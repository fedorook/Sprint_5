from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.locators import RegistrationPageLocators, MainPageLocators, ProfilePageLocators, LoginPageLocators
from src.utils import generate_unique_email, login, is_logged_in
from src.config import Config


def test_successful_registration(driver):
    driver.get(Config.REGISTRATION_URL)

    # Generate unique test data
    email = generate_unique_email()
    password = "password"

    # Fill out registration form
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Sergei")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Wait for redirect to login page
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
    )

    # Log in with the newly created account
    login(driver, email, password)

    # Assert we're logged in
    is_logged_in(driver)


def test_registration_with_invalid_password(driver):
    driver.get(Config.REGISTRATION_URL)

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Sergei")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_unique_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("12345")  # too short
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Expect some error message (you may want to locate the actual error if known)
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")
        )
    )
    assert error.is_displayed()
