from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Selectors:
    AUTH_FORM_TITLE = (By.CSS_SELECTOR, ".panel-title")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASS_INPUT = (By.CSS_SELECTOR, "#input-password")
    FORGOT_PASS_BTN = (By.CSS_SELECTOR, ".help-block")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type=submit]")


# Тест на проверку видимости элемента "заголовок формы аутентификации" на странице входа в админку
def test_form_title_visibility(browser, auth_url):
    browser.get(auth_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-title")))
    time.sleep(5)
    assert browser.find_element(
        *Selectors.AUTH_FORM_TITLE) == element, "Needs form title 'element' to be found on the page!"


# Тест на проверку видимости элемента "поле ввода логина" на странице входа в админку
def test_login_input_visibility(browser, auth_url):
    browser.get(auth_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    assert browser.find_element(
        *Selectors.LOGIN_INPUT) == element, "Needs login input 'element' to be found on the page!"


# Тест на проверку видимости элемента "поле ввода пароля" на странице входа в админку
def test_password_input_visibility(browser, auth_url):
    browser.get(auth_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    assert browser.find_element(
        *Selectors.PASS_INPUT) == element, "Needs password input 'element' to be found on the page!"


# Тест на проверку видимости элемента "ссылка Забыли пароль" на странице входа в админку
def test_forgot_password_visibility(browser, auth_url):
    browser.get(auth_url)
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".help-block")))
    assert browser.find_element(
        *Selectors.FORGOT_PASS_BTN) == element, "Needs forgot password 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка Войти" на странице входа в админку
def test_login_btn_visibility(browser, auth_url):
    browser.get(auth_url)
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type=submit]")))
    assert browser.find_element(
        *Selectors.LOGIN_BTN) == element, "Needs login button 'element' to be found on the page!"
