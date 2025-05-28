from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # метод регистрации нового юзера
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        reg_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        reg_password.send_keys(password)
        reg_confirm_password.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()

    # Проверка находимся ли мы сейчас на странице логина
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'incorrect URL'

    # Проверка есть ли на странице форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    # Проверка есть ли на странице форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form not found'
