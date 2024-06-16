from selenium.webdriver.common.by import By


class BasePage:

    FOOTER = (By.TAG_NAME, 'footer')
    SUB_ELEMENTS_LIST = (By.CLASS_NAME, 'element-list')
    SUB_ELEMENTS_ITEM = (By.TAG_NAME, 'li')
    MENU_LIST = (By.CLASS_NAME, 'menu-list')


class MainPageLocators(BasePage):
    BANNER = (By.CLASS_NAME, 'home-banner')
    CARD_ITEM = (By.CLASS_NAME, 'top-card')
    CARD_BODY = (By.CLASS_NAME, 'card-body')
    LINK = (By.TAG_NAME, 'a')


class ElementsPage(BasePage):
    ELEMENTS_LIST = (By.CLASS_NAME, 'element-group')


class TextBoxPage(BasePage):
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT = (By.ID, 'submit')
    OUTPUT = (By.ID, 'output')
    TEXT_ITEM = (By.TAG_NAME, 'p')
    FILED_ERROR = (By.CLASS_NAME, 'field-error')


class BookStorePage(BasePage):
    LOGIN_ITEM = (By.ID, 'item-0')


class LoginPage(BasePage):
    NEW_USER = (By.ID, 'newUser')


class RegisterPage(BasePage):
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    USERNAME = (By.ID, 'userName')
    PASSWORD = (By.ID, 'password')
    CAPTCHA = (By.ID, 'g-recaptcha')
    REGISTER_BUTTON = (By.ID, 'register')
