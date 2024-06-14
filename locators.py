from selenium.webdriver.common.by import By


class MainPageLocators:
    FOOTER = (By.TAG_NAME, 'footer')
    BANNER = (By.CLASS_NAME, 'home-banner')
    CARD_ITEM = (By.CLASS_NAME, 'top-card')
    CARD_BODY = (By.CLASS_NAME, 'card-body')
    LINK = (By.TAG_NAME, 'a')
