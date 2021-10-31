from page_objects.BasePage import BasePage
from page_objects.elements.Header import Header
from page_objects.MainPage import MainPageLocators
from page_objects.TestData import MainPageTestData
from page_objects.TestData import HeaderTestData


# Тест на проверку видимости элемента "слайдер" на главной странице
def test_slider_visibility(browser, base_url):
    main_page = BasePage(browser, base_url)
    main_page.go_to_site()
    element = main_page.find_element(MainPageLocators.MAIN_SLIDER, 2)
    assert MainPageTestData.MAIN_SLIDER_ID == main_page.get_property(element, 'id'),\
        "Element id should be equal to 'slideshow0'!"


# Тест на проверку видимости элемента "корзина" на главной странице
def test_cart_visibility(browser, base_url):
    main_page = BasePage(browser, base_url)
    main_page.go_to_site()
    element = main_page.find_element(MainPageLocators.CART, 2)
    assert MainPageTestData.CART_ID == main_page.get_property(element, 'id'), "Element id should be equal to 'cart'!"


# Тест на проверку видимости элемента "поиск" на главной странице
def test_search_visibility(browser, base_url):
    main_page = BasePage(browser, base_url)
    main_page.go_to_site()
    element = main_page.find_element(MainPageLocators.SEARCH, 2)
    assert MainPageTestData.SEARCH_ID == main_page.get_property(element, 'id'), \
        "Element id should be equal to 'search'!"


# Тест на проверку видимости элемента "карусель логотипов" на главной странице
def test_logo_carousel_visibility(browser, base_url):
    main_page = BasePage(browser, base_url)
    main_page.go_to_site()
    element = main_page.find_element(MainPageLocators.LOGO_CAROUSEL, 2)
    assert MainPageTestData.LOGO_CAROUSEL_ID == main_page.get_property(element, 'id'), \
        "Element id should be equal to 'carousel0'!"


# Тест на проверку видимости 4 продуктовых карточек на главной странице
def test_products_visibility(browser, base_url):
    main_page = BasePage(browser, base_url)
    main_page.go_to_site()
    assert MainPageTestData.PRODUCT_CLASS_QTY == main_page.get_quantity(MainPageLocators.PRODUCTS),\
        "Quantity of elements should be equal to 4!"


# Тест на проверку переключения валюты на Евро
def test_change_currency_to_eur(browser, base_url):
    main_page = Header(browser, base_url)
    main_page.go_to_site()
    main_page.change_currency_to('EUR')
    euro_cur = main_page.find_element(Header.CURRENCY_SIGN, 3)
    assert HeaderTestData.EURO_SIGN_CHECK == main_page.get_property(euro_cur, 'innerHTML'),\
        "Currency sign should be equal to '€'!"


# Тест на проверку переключения валюты на Фунты
def test_change_currency_to_gbp(browser, base_url):
    main_page = Header(browser, base_url)
    main_page.go_to_site()
    main_page.change_currency_to('GBP')
    gbp_cur = main_page.find_element(Header.CURRENCY_SIGN, 3)
    assert HeaderTestData.GBP_SIGN_CHECK == main_page.get_property(gbp_cur, 'innerHTML'), \
        "Currency sign should be equal to '£'!"


# Тест на проверку переключения валюты на Доллары
def test_change_currency_to_usd(browser, base_url):
    main_page = Header(browser, base_url)
    main_page.go_to_site()
    main_page.change_currency_to('USD')
    usd_cur = main_page.find_element(Header.CURRENCY_SIGN, 3)
    assert HeaderTestData.USD_SIGN_CHECK == main_page.get_property(usd_cur, 'innerHTML'), \
        "Currency sign should be equal to '$'!"


# Тест на проверку переключения валюты на Фунты с пользовательским движением мышкой
def test_user_change_currency(browser, base_url):
    main_page = Header(browser, base_url)
    main_page.go_to_site()
    main_page.simple_click(Header.CURRENCY_BTN)
    main_page.move_and_click(Header.GBP)
