import pytest
from .pages.product_page import ProductPage
import time

def test_guest_can_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    # Получаем название и цену товара
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Добавляем товар в корзину
    page.add_to_cart()

    # Решаем капчу
    page.solve_quiz_and_get_code()
    time.sleep(10)

    # Проверяем название и цену
    page.should_be_correct_product_added(product_name)
    page.should_be_correct_price(product_price)