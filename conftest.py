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
    parser.addoption("--base_url", action="store", default="https://demo.opencart.com")
    parser.addoption("--cat_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/category&path=18")
    parser.addoption("--prod_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44")
    parser.addoption("--auth_url", action="store",
                     default="https://demo.opencart.com/admin/")
    parser.addoption("--local_base_url", action="store", default="http://127.0.0.1:8081/")
    parser.addoption("--local_admin_url", action="store", default="http://127.0.0.1:8081/admin/")
    parser.addoption("--local_register_url", action="store",
                     default="http://127.0.0.1:8081/index.php?route=account/register")


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--base_url")


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
def local_base_url(request):
    return request.config.getoption("--local_base_url")


@pytest.fixture(scope='session')
def local_admin_url(request):
    return request.config.getoption("--local_admin_url")


@pytest.fixture(scope='session')
def local_register_url(request):
    return request.config.getoption("--local_register_url")


@pytest.fixture(scope='session')
def browser(request):
    _browser = request.config.getoption("--browser_driver")
    maximized = request.config.getoption("--maximized")
    driver = None
    if _browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif _browser == "opera":
        driver = webdriver.Opera(OperaDriverManager().install())
    elif _browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif _browser == "safari":
        driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()
    request.addfinalizer(final)
    return driver
