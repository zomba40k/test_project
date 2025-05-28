from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Добавляет в корзину товар на странице которого мы находимся
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    # Возвращает название товара
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Возвращает цену
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # Проверяет совпадает ли название товара в сообщении ожидаемому
    def should_be_correct_product_added(self, expected_product_name):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_product_name == success_message, f"Product name '{expected_product_name}' doesn't match message '{success_message}'"

    # Проверяет совпадает ли цена в корзине ожидаемой
    def should_be_correct_price(self, expected_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert expected_price == basket_total, f"Basket price '{basket_total}' doesn't match product price '{expected_price}'"

    # Проверяет исчезло ли сообщение об успешном добавлении в корзину
    def had_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message should disappear'

    # Проверяет нет ли сообщения об успешном добавлении в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message should not be displayed'
