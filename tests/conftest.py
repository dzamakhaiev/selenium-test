import pytest
from drivers import ChromeDriver, EdgeDriver
from logger import logger


pytest_logger = logger.Logger('test', level='DEBUG')


@pytest.fixture(params=['chrome', 'edge'], scope="function")
def driver(request):
    pytest_logger.info(f'Test "{request.node.name}" started for browser "{request.param}"')

    if request.param == 'chrome':
        driver = ChromeDriver()
    elif request.param == 'edge':
        driver = EdgeDriver()
    else:
        raise NotImplementedError

    yield driver
    driver.quit_driver()
    pytest_logger.info(f'Test "{request.node.name}" completed.')
