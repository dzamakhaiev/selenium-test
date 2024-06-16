import pytest
import test_data
import pages


def find_item(items, exp_text):
    for item in items:
        if exp_text in item.text:
            return item
    else:
        assert False


def test_new_user_scenario(driver):
    main_page = pages.MainPage(driver)
    main_page.go_to_main_page()
    assert main_page.get_current_url() == test_data.MainPage.EXP_URL

    # Get list of cards and click on Book Store card
    cards = main_page.get_list_of_cards()
    card = find_item(cards, test_data.MainPage.BOOK_STORE_CARD)
    card.click()

    # Find login item in Book Store card
    book_page = pages.BookStorePage(driver)
    assert book_page.get_current_url() == test_data.BookStorePage.EXP_URL
    items = book_page.get_menu_item_list(exp_text=test_data.MainPage.BOOK_STORE_CARD)
    login_item = find_item(items, test_data.BookStorePage.LOGIN_TEXT)
    login_item.click()

    # Check new user page and click on New user button
    login_page = pages.LoginPage(driver)
    assert login_page.get_current_url() == test_data.LoginPage.EXP_URL
    button = login_page.get_new_user_button()
    assert button
    button.click()

    # Check register page and create new user
    register_page = pages.RegisterPage(driver)
    assert register_page.get_current_url() == test_data.RegisterPage.EXP_URL
    reg_dict = {'first_name': 'test_name', 'last_name': 'test_surname',
                'username': 'test_user', 'password': 'Test12345!'}
    register_page.fill_register_form(reg_dict)

    # Find and click on captcha
    captcha = register_page.get_captcha()
    assert captcha
    captcha.click()

    # Find register button and click on it
    button = register_page.get_register_button()
    assert button
    button.click()

    # Switch on alert and close it
    alert = register_page.get_alert()
    assert alert
    alert.accept()

    # Log in as new user
    login_page.go_lo_login_page()
    assert login_page.get_current_url() == test_data.LoginPage.EXP_URL
    login_page.fill_username_and_password(username=reg_dict['username'], password=reg_dict['password'])

    button = login_page.get_login_button()
    assert button
    button.click()

    # Check profile page
    profile_page = pages.ProfilePage(driver)
    assert profile_page.get_current_url() == test_data.ProfilePage.EXP_URL

    # Get Delete account button and click on it
    buttons = profile_page.get_buttons()
    button = find_item(buttons, test_data.ProfilePage.DELETE_ACCOUNT)
    assert button
    button.click()

    # Check redirect on login page
    assert login_page.get_current_url() == test_data.LoginPage.EXP_URL


if __name__ == '__main__':
    pytest.main()
