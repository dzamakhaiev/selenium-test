import pytest
from drivers import ChromeDriver, EdgeDriver


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        driver = ChromeDriver()
    elif request.param == 'edge':
        driver = EdgeDriver()
    else:
        raise NotImplementedError

    yield driver
