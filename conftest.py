import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Запуск браузера в безголовом режиме")
    parser.addoption('--language', action='store', default=None, help="Say language name to select")

@pytest.fixture
def browser(request):
    options = Options()
    lang= request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    # Проверяем, передан ли --headless
    if request.config.getoption("--headless"):
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
