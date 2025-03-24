from selenium.webdriver.common.by import By

class ConstructorSectionLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    GO_TO_REGISTRATION = (By.XPATH, "//a[text()='Зарегистрироваться']")
    GO_TO_PASSWORD_RESET = (By.XPATH, "//a[text()='Восстановить пароль']")

class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_FROM_MAIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

class RegistrationPageLocators:
    GO_TO_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

class PasswordRecoveryPageLocators:
    GO_TO_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")
