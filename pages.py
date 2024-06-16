import locators
from drivers import ChromeDriver, EdgeDriver
from logger import logger

page_logger = logger.Logger('test', level='DEBUG')


class BasePage:

    def __init__(self, driver: (ChromeDriver, EdgeDriver)):
        self.driver = driver

    def get_current_url(self):
        return self.driver.get_current_url()

    def get_page_title(self):
        page_logger.info('Finding title for current page.')
        return self.driver.get_title()

    def get_page_footer(self, locator):
        page_logger.info('Finding footer for current page.')
        return self.driver.find_element(locator)

    def find_link(self, element, locator):
        page_logger.info('Finding link for current element.')
        return self.driver.find_element(element=element, locator=locator)

    def find_field_error(self, locator):
        page_logger.info('Finding error for current element.')
        return self.driver.find_element(locator=locator)

    def get_menu_item_list(self, exp_text):
        elements = self.driver.find_elements(locator=locators.ElementsPage.ELEMENTS_LIST)
        for element in elements:
            if exp_text in element.text:
                break
        else:
            return []

        element = self.driver.find_element(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_LIST)
        elements = self.driver.find_elements(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_ITEM)
        return elements

    def get_buttons(self, locator):
        return self.driver.find_elements(locator=locator)


class MainPage(BasePage):
    url = 'https://demoqa.com/'

    def __init__(self, driver: (ChromeDriver, EdgeDriver)):
        page_logger.info('Main page created.')
        super().__init__(driver)

    def go_to_main_page(self):
        self.driver.go_to(self.url)

    def get_page_footer(self, locator=locators.MainPageLocators.FOOTER):
        return super().get_page_footer(locator)

    def get_banner(self):
        page_logger.info('Finding banner on main page.')
        return self.driver.find_element(locators.MainPageLocators.BANNER)

    def find_banner_link(self, element, locator=locators.MainPageLocators.LINK):
        page_logger.info('Finding banner link.')
        return super().find_link(element=element, locator=locator)

    def get_list_of_cards(self):
        page_logger.info('Finding cards on main page.')
        elements = self.driver.find_elements(locator=locators.MainPageLocators.CARD_ITEM)
        return elements


class ElementsPage(BasePage):
    url = 'https://demoqa.com/elements'

    def __init__(self, driver: (ChromeDriver, EdgeDriver)):
        page_logger.info('Elements page created.')
        super().__init__(driver)

    def go_to_elements_page(self):
        self.driver.go_to(self.url)

    def get_page_footer(self, locator=locators.ElementsPage.FOOTER):
        return super().get_page_footer(locator)

    def get_elements_list(self):
        page_logger.info('Finding item list on elements page.')
        element = self.driver.find_element(locator=locators.ElementsPage.ELEMENTS_LIST)
        element = self.driver.find_element(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_LIST)
        elements = self.driver.find_elements(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_ITEM)
        return elements


class TextBoxPage(BasePage):
    url = 'https://demoqa.com/text-box'

    def __init__(self, driver: (ChromeDriver, EdgeDriver)):
        page_logger.info('Text Box page created.')
        super().__init__(driver)

    def go_to_text_box_page(self):
        self.driver.go_to(self.url)

    def get_page_footer(self, locator=locators.TextBoxPage.FOOTER):
        return super().get_page_footer(locator)

    def fill_text_fields(self, field_dict: dict):
        page_logger.info('Sending text in Text Box on elements page and click Submit.')
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
        page_logger.info('Reading text output from Text Box on elements page.')
        output = self.driver.find_element(locator=locators.TextBoxPage.OUTPUT)
        text_items = self.driver.find_elements(element=output, locator=locators.TextBoxPage.TEXT_ITEM)
        return text_items

    def find_field_error(self, locator=locators.TextBoxPage.FILED_ERROR):
        page_logger.info('Finding element with error class for Text Box on elements page.')
        return super().find_field_error(locator=locator)


class BookStorePage(BasePage):
    url = 'https://demoqa.com/books'


class LoginPage(BasePage):
    url = 'https://demoqa.com/login'

    def go_lo_login_page(self):
        self.driver.go_to(self.url)

    def fill_username_and_password(self, username, password):
        username_filed = self.driver.find_element(locator=locators.LoginPage.USERNAME)
        password_filed = self.driver.find_element(locator=locators.LoginPage.PASSWORD)
        username_filed.send_keys(username)
        password_filed.send_keys(password)

    def get_login_button(self):
        return self.driver.find_element(locator=locators.LoginPage.LOGIN)

    def get_new_user_button(self):
        return self.driver.find_element(locator=locators.LoginPage.NEW_USER)


class RegisterPage(BasePage):
    url = 'https://demoqa.com/register'

    def fill_register_form(self, reg_dict: dict):
        first_name = self.driver.find_element(locator=locators.RegisterPage.FIRST_NAME)
        last_name = self.driver.find_element(locator=locators.RegisterPage.LAST_NAME)
        username = self.driver.find_element(locator=locators.RegisterPage.USERNAME)
        password = self.driver.find_element(locator=locators.RegisterPage.PASSWORD)

        first_name.send_keys(reg_dict.get('first_name'))
        last_name.send_keys(reg_dict.get('last_name'))
        username.send_keys(reg_dict.get('username'))
        password.send_keys(reg_dict.get('password'))

    def get_captcha(self):
        return self.driver.find_element(locator=locators.RegisterPage.CAPTCHA)

    def get_register_button(self):
        return self.driver.find_element(locator=locators.RegisterPage.REGISTER_BUTTON)

    def get_alert(self):
        alert = self.driver.switch_to_alert()
        return alert


class ProfilePage(BasePage):
    url = 'https://demoqa.com/profile'

    def get_buttons(self, locator=locators.ProfilePage.BUTTON):
        return super().get_buttons(locator)
