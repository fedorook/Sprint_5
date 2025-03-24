from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import LoginPageLocators, MainPageLocators, ProfilePageLocators
import random

def generate_unique_email():
    random_digits = random.randint(100, 999)
    return f"sergeifedoruk19{random_digits}@ya.ru"

def login(driver, email, password, wait_time=10):
    wait = WebDriverWait(driver, wait_time)

    email_input = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys(password)

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    # Wait until we’re back on main page (personal account is visible)
    wait.until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))

def is_logged_in(driver, wait_time=5):
    wait = WebDriverWait(driver, wait_time)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    wait.until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
