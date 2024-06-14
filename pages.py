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

    def find_field_error(self, locator):
        return self.driver.find_element(locator=locator)


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


class ElementsPage(BasePage):

    url = 'https://demoqa.com/elements'

    def go_to_elements_page(self):
        self.driver.go_to(self.url)

    def get_page_footer(self, locator=locators.ElementsPage.FOOTER):
        return super().get_page_footer(locator)

    def get_elements_list(self):
        element = self.driver.find_element(locator=locators.ElementsPage.ELEMENTS_LIST)
        element = self.driver.find_element(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_LIST)
        elements = self.driver.find_elements(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_ITEM)
        return elements


class TextBoxPage(BasePage):

    url = 'https://demoqa.com/text-box'

    def go_to_text_box_page(self):
        self.driver.go_to(self.url)

    def get_page_footer(self, locator=locators.TextBoxPage.FOOTER):
        return super().get_page_footer(locator)

    def fill_text_fields(self, field_dict: dict):
        name_field = self.driver.find_element(locator=locators.TextBoxPage.FULL_NAME)
        email_field = self.driver.find_element(locator=locators.TextBoxPage.EMAIL)
        current_field = self.driver.find_element(locator=locators.TextBoxPage.CURRENT_ADDRESS)
        permanent_field = self.driver.find_element(locator=locators.TextBoxPage.PERMANENT_ADDRESS)

        name_field.send_keys(field_dict.get('full_name', ''))
        email_field.send_keys(field_dict.get('email', ''))
        current_field.send_keys(field_dict.get('current_address', ''))
        permanent_field.send_keys(field_dict.get('permanent_address', ''))

        self.driver.find_element(locator=locators.TextBoxPage.SUBMIT).click()

    def read_output(self):
        output = self.driver.find_element(locator=locators.TextBoxPage.OUTPUT)
        text_items = self.driver.find_elements(element=output, locator=locators.TextBoxPage.TEXT_ITEM)
        return text_items

    def find_field_error(self, locator=locators.TextBoxPage.FILED_ERROR):
        return super().find_field_error(locator=locator)