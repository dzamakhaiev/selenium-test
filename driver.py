from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import settings


def no_such_element_exception(find):
    def wrap(self, *args, **kwargs):
        try:
            return find(self, *args, **kwargs)
        except NoSuchElementException:
            return None
    return wrap


class BaseDriver:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.implicitly_wait(settings.IMP_WAIT_TIME)
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def set_driver(self, driver: webdriver.Chrome):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    @no_such_element_exception
    def find_element(self, locator, element=None):
        if not element:
            return self.driver.find_element(*locator)
        else:
            return element.find_element(*locator)

    def click_on_element(self, locator=None, element=None):
        if not locator and element:
            element.click()
        else:
            self.find_element(locator, element).click()

    def input_text(self, locator, text, element=None):
        field = self.find_element(locator, element)
        field.send_keys(text)

    def __del__(self):
        self.driver.quit()


class ChromeDriver(BaseDriver):

    def __init__(self):
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(service=service)
        super().__init__(driver)
