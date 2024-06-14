import locators
from drivers import ChromeDriver


class BasePage:

    def __init__(self, driver: ChromeDriver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.get_current_url()

    def get_page_title(self):
        return self.driver.get_title()


class MainPage(BasePage):
    url = 'https://demoqa.com/'

    def __init__(self, driver: ChromeDriver):
        super().__init__(driver)

    def go_to_main_page(self):
        self.driver.go_to(self.url)

    def get_list_of_cards(self):
        elements = self.driver.find_elements(locator=locators.MainPageLocators.CARD_ITEM)
        return elements
