import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions




# Добавляем параметр language и browser_name
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb", help="if --language not chosen used eng-gb")
    parser.addoption("--browser_name", action="store", default="chrome", help="--browser_name should be chrome or firefox")


@pytest.fixture
def user_language(request):
    return request.config.getoption("language")

# Фикстура браузера с учетом языка
@pytest.fixture
def browser(user_language,request):
    browser_name = request.config.getoption("browser_name")


    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        profile.update_preferences()
        options.profile = profile
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("--browser_name должен быть chrome или firefox")
    yield browser
    browser.quit()