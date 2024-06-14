from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import settings
from logger import logger


driver_logger = logger.Logger('driver', level='DEBUG')


def no_such_element_exception(find):
    def wrap(self, *args, **kwargs):

        try:
            return find(self, *args, **kwargs)
        except NoSuchElementException as e:
            driver_logger.error(e)
            return None

    return wrap


class BaseDriver:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, driver: (webdriver.Chrome, webdriver.Edge)):
        browser_name = driver.capabilities['browserName']
        browser_version = driver.capabilities.get('browserVersion') or driver.capabilities.get('version')
        driver_logger.info(f'Driver started: {browser_name} {browser_version}')

        self.driver = driver
        self.driver.implicitly_wait(settings.IMP_WAIT_TIME)
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def set_driver(self, driver: (webdriver.Chrome, webdriver.Edge)):
        self.driver = driver

    def go_to(self, url):
        driver_logger.info(f'Driver is loading url: {url}')
        self.driver.get(url)

    def get_current_url(self):
        driver_logger.info(f'Driver is returning current url: {self.driver.current_url}')
        return self.driver.current_url

    def get_title(self):
        driver_logger.info(f'Driver is returning page title: {self.driver.title}')
        return self.driver.title

    @no_such_element_exception
    def find_element(self, locator, element=None):
        driver_logger.debug(f'Driver is finding element by locator: {locator}')

        if not element:
            return self.driver.find_element(*locator)
        else:
            return element.find_element(*locator)

    @no_such_element_exception
    def find_elements(self, locator, element=None):
        driver_logger.debug(f'Driver is finding elements by locator: {locator}')

        if not element:
            return self.driver.find_elements(*locator)
        else:
            return element.find_elements(*locator)

    def click_on_element(self, locator=None, element=None):
        driver_logger.debug(f'Driver is clicking on element using locator: {locator}')
        if not locator and element:
            element.click()
        else:
            self.find_element(locator, element).click()

    def input_text(self, locator, text, element=None):
        driver_logger.debug(f'Driver is sending text "{text}" in element using locator: {locator}')
        field = self.find_element(locator, element)
        field.send_keys(text)

    def quit_driver(self):
        self.driver.quit()
        driver_logger.info('Driver closed.')

    def __del__(self):
        self.quit_driver()


class ChromeDriver(BaseDriver):

    def __init__(self):
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(service=service)
        super().__init__(driver)


class EdgeDriver(BaseDriver):

    def __init__(self):
        service = webdriver.EdgeService()
        driver = webdriver.Edge(service=service)
        super().__init__(driver)
