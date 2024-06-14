from selenium.webdriver.common.by import By


class BasePage:

    FOOTER = (By.TAG_NAME, 'footer')
    SUB_ELEMENTS_LIST = (By.CLASS_NAME, 'element-list')
    SUB_ELEMENTS_ITEM = (By.TAG_NAME, 'li')


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
