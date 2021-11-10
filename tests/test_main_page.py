from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selectors:
    MAIN_SLIDER = (By.CSS_SELECTOR, "#slideshow0")
    CART = (By.CSS_SELECTOR, "#cart")
    SEARCH = (By.CSS_SELECTOR, "#search")
    LOGO_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout")


# Тест на проверку видимости элемента "слайдер" на главной странице
def test_slider_visibility(browser, url_base):
    browser.get(url_base)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#slideshow0")))
    assert browser.find_element(*Selectors.MAIN_SLIDER) == element, "Needs slider 'element' to be found on the page!"


# Тест на проверку видимости элемента "корзина" на главной странице
def test_cart_visibility(browser, url_base):
    browser.get(url_base)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart")))
    assert browser.find_element(*Selectors.CART) == element, "Needs cart 'element' to be found on the page!"


# Тест на проверку видимости элемента "поиск" на главной странице
def test_search_visibility(browser, url_base):
    browser.get(url_base)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search")))
    assert browser.find_element(*Selectors.SEARCH) == element, "Needs search 'element' to be found one the page!"


# Тест на проверку видимости элемента "карусель логотипов" на главной странице
def test_logo_swiper_visibility(browser, url_base):
    browser.get(url_base)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#carousel0")))
    assert browser.find_element(
        *Selectors.LOGO_CAROUSEL) == element, "Needs logo carousel 'element' to be found one the page!"


# Тест на проверку видимости 4 продуктовых карточек на главной странице
def test_products_visibility(browser, url_base):
    browser.get(url_base)
    elements = WebDriverWait(browser, 1).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    assert len(elements) == 4, "Needs 4 products cards 'element' to be found one the page!"
