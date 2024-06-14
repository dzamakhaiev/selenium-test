import pytest
import test_data
import pages


def test_elements_page(driver):
    elements_page = pages.ElementsPage(driver)
    elements_page.go_to_elements_page()
    footer = elements_page.get_page_footer()

    assert elements_page.get_current_url() == test_data.ElementsPage.EXP_URL
    assert elements_page.get_page_title() == test_data.ElementsPage.EXP_TITLE
    assert footer.text == test_data.ElementsPage.EXP_FOOTER


def test_elements_list(driver):
    elements_page = pages.ElementsPage(driver)
    elements_page.go_to_elements_page()
    item_list = elements_page.get_elements_list()
    item_list = [item.text for item in item_list]

    assert item_list == test_data.ElementsPage.EXP_ITEM_LIST


if __name__ == '__main__':
    pytest.main()
