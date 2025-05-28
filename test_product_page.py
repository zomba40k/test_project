import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.parametrize("promo", [
    'offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',
    pytest.param('offer7', marks=pytest.mark.xfail),'offer8', 'offer9'])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    # Получаем название и цену товара
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Добавляем товар в корзину
    page.add_to_cart()

    # Решаем капчу
    page.solve_quiz_and_get_code()
    # Проверяем название и цену
    try:

        page.should_be_correct_product_added(product_name)
        page.should_be_correct_price(product_price)

    except AssertionError:
        print(f"Test failed on URL: {link}")
        raise

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.should_not_be_items_in_basket()
    cart_page.should_be_empty_basket_text()


