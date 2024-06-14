import pytest
import test_data
import pages


def test_main_page(driver):
    main_page = pages.MainPage(driver)
    main_page.go_to_main_page()

    assert main_page.url == main_page.get_current_url()
    assert main_page.get_page_title() == test_data.MainPage.EXP_TITLE


if __name__ == '__main__':
    pytest.main()
