from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selectors:
    ASIDE_MENU = (By.CSS_SELECTOR, "#column-left")
    BANNER = (By.CSS_SELECTOR, "#banner0")
    LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")
    GRID_VIEW_BTN = (By.CSS_SELECTOR, "#grid-view")
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout")


# Тест на проверку видимости элемента "боковое меню" на странице каталога
def test_aside_menu_visibility(browser, cat_url):
    browser.get(cat_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-left")))
    assert browser.find_element(*Selectors.ASIDE_MENU) == element, "Needs aside menu 'element' to be found on the page!"


# Тест на проверку видимости элемента "баннер" на странице каталога
def test_banner_visibility(browser, cat_url):
    browser.get(cat_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#banner0")))
    assert browser.find_element(*Selectors.BANNER) == element, "Needs banner 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка вывода - list" на странице каталога
def test_list_btn_visibility(browser, cat_url):
    browser.get(cat_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#list-view")))
    assert browser.find_element(
        *Selectors.LIST_VIEW_BTN) == element, "Needs list button 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка вывода - grid" на странице каталога
def test_grid_btn_visibility(browser, cat_url):
    browser.get(cat_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#grid-view")))
    assert browser.find_element(
        *Selectors.GRID_VIEW_BTN) == element, "Needs grid button 'element' to be found on the page!"


# Тест на проверку видимости 5 продуктовых карточек на странице каталога с товарами
def test_products_visibility(browser, cat_url):
    browser.get(cat_url)
    elements = WebDriverWait(browser, 1).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    assert len(elements) == 5, "Needs 5 product cards 'element' to be found one the page!"
