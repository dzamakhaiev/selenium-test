import locators
from drivers import ChromeDriver


class BasePage:

    def __init__(self, driver: ChromeDriver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.get_current_url()

    def get_page_title(self):
        return self.driver.get_title()

    def get_page_footer(self, locator):
        return self.driver.find_element(locator)

    def find_link(self, element, locator):
        return self.driver.find_element(element=element, locator=locator)


class MainPage(BasePage):
    url = 'https://demoqa.com/'

    def __init__(self, driver: ChromeDriver):
        super().__init__(driver)

    def go_to_main_page(self):
        self.driver.go_to(self.url)

    def get_page_footer(self, locator=locators.MainPageLocators.FOOTER):
        return super().get_page_footer(locator)

    def get_banner(self):
        return self.driver.find_element(locators.MainPageLocators.BANNER)

    def find_banner_link(self, element, locator=locators.MainPageLocators.LINK):
        return super().find_link(element=element, locator=locator)

    def get_list_of_cards(self):
        elements = self.driver.find_elements(locator=locators.MainPageLocators.CARD_ITEM)
        return elements
