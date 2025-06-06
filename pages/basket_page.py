from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверка на отсутствие товаров в корзине
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'There is items in basket'

    # Проверка на присутствие сообщения об пустой корзине в корзине
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), 'There is empty basket text'
