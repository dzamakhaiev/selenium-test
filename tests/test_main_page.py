import pytest
import test_data
import pages


def test_main_page(driver):
    main_page = pages.MainPage(driver)
    main_page.go_to_main_page()

    assert main_page.get_current_url() == test_data.MainPage.EXP_URL
    assert main_page.get_page_title() == test_data.MainPage.EXP_TITLE


def test_main_page_elements(driver):
    main_page = pages.MainPage(driver)
    main_page.go_to_main_page()

    elements = main_page.get_list_of_cards()
    cards = [element.text for element in elements]
    assert cards == test_data.MainPage.EXP_CARDS


if __name__ == '__main__':
    pytest.main()
