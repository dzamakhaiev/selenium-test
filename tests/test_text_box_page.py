import pytest
import test_data
import pages


def test_text_box_page(driver):
    text_page = pages.TextBoxPage(driver)
    text_page.go_to_text_box_page()
    footer = text_page.get_page_footer()

    assert text_page.get_current_url() == test_data.TextBoxPage.EXP_URL
    assert text_page.get_page_title() == test_data.TextBoxPage.EXP_TITLE
    assert footer.text == test_data.TextBoxPage.EXP_FOOTER


def test_text_field(driver):
    text_page = pages.TextBoxPage(driver)
    text_page.go_to_text_box_page()

    text_dict = {'full_name': 'test_user', 'email': 'test@email.com',
                 'current_address': 'some_address', 'permanent_address': 'another_address'}
    text_page.fill_text_fields(text_dict)
    text_items = text_page.read_output()
    text_items = [item.text.split(':')[-1] for item in text_items]

    for value in text_dict.values():
        assert value in text_items


if __name__ == '__main__':
    pytest.main()
