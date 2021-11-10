import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run tests headless")
    parser.addoption("--browser_driver", action="store", default="chrome", choices=["chrome", "opera", "firefox",
                                                                                    "safari"])
    parser.addoption("--url_base", action="store", default="https://demo.opencart.com")
    parser.addoption("--cat_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/category&path=18")
    parser.addoption("--prod_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44")
    parser.addoption("--auth_url", action="store", default="https://demo.opencart.com/admin/")


@pytest.fixture(scope='session')
def url_base(request):
    return request.config.getoption("--url_base")


@pytest.fixture(scope='session')
def cat_url(request):
    return request.config.getoption("--cat_url")


@pytest.fixture(scope='session')
def prod_url(request):
    return request.config.getoption("--prod_url")


@pytest.fixture(scope='session')
def auth_url(request):
    return request.config.getoption("--auth_url")


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption("--browser_driver")
    maximized = request.config.getoption("--maximized")
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "opera":
        driver = webdriver.Opera(OperaDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser == "safari":
        driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()
    request.addfinalizer(final)
    return driver
