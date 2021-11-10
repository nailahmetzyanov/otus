from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selectors:
    THUMB_ELEM = (By.CSS_SELECTOR, ".thumbnails")
    THUMB_QTY = (By.CSS_SELECTOR, ".thumbnail")
    PROD_TITLE = (By.CSS_SELECTOR, "div.btn-group + h1")
    QTY_INPUT = (By.CSS_SELECTOR, "input[name = \"quantity\"]")
    CART_BTN = (By.CSS_SELECTOR, "#button-cart")


# Тест на проверку видимости элемента "все изображения товара в одном блоке" на странице товара
def test_thumbnail_visibility(browser, prod_url):
    browser.get(prod_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".thumbnails")))
    assert browser.find_element(
        *Selectors.THUMB_ELEM) == element, "Needs main thumbnail 'element' to be found on the page!"


# Тест на проверку видимости 4х элементов "изображения товара" на странице товара
def test_thumbnails_qty_visibility(browser, prod_url):
    browser.get(prod_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".thumbnail")))
    assert len(element) == 4, "Needs 4 thumbnails 'element' to be found on the page!"


# Тест на проверку видимости элемента "название товара" на странице товара
def test_product_title_visibility(browser, prod_url):
    browser.get(prod_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.btn-group + h1")))
    assert browser.find_element(
        *Selectors.PROD_TITLE) == element, "Needs product title 'element' to be found on the page!"


# Тест на проверку видимости элемента "поле для ввода количества товаров" на странице товара
def test_quantity_input_visibility(browser, prod_url):
    browser.get(prod_url)
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name = \"quantity\"]")))
    assert browser.find_element(
        *Selectors.QTY_INPUT) == element, "Needs quantity of goods input 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка положить в корзину" на странице товара
def test_cart_btn_visibility(browser, prod_url):
    browser.get(prod_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    assert browser.find_element(*Selectors.CART_BTN) == element, "Needs cart button 'element' to be found on the page!"
