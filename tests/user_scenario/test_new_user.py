import pytest
import test_data
import pages


def test_new_user(driver):
    main_page = pages.MainPage(driver)
    main_page.go_to_main_page()
    assert main_page.get_current_url() == test_data.MainPage.EXP_URL

    # Get list of cards and click on Book Store card
    cards = main_page.get_list_of_cards()
    for card in cards:
        if test_data.MainPage.BOOK_STORE_CARD in card.text:
            card.click()


if __name__ == '__main__':
    pytest.main()
