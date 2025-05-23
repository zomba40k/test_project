import time
import pytest
from selenium.webdriver.common.by import By


def test_is_button_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.")
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    assert button.is_displayed(), 'Кнопка не найдена'

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
