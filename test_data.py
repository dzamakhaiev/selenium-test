class BasePage:

    EXP_TITLE = 'DEMOQA'
    EXP_FOOTER = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


class MainPage(BasePage):

    EXP_URL = 'https://demoqa.com/'
    EXP_BANNER_URL = 'https://www.toolsqa.com/selenium-training/'
    EXP_CARDS = ['Elements', 'Forms', 'Alerts, Frame & Windows', 'Widgets', 'Interactions', 'Book Store Application']


class ElementsPage(BasePage):

    EXP_URL = 'https://demoqa.com/elements'
    EXP_ITEM_LIST = ['Text Box', 'Check Box', 'Radio Button', 'Web Tables', 'Buttons', 'Links', 'Broken Links - Images',
                     'Upload and Download', 'Dynamic Properties']
