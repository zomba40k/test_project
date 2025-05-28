import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    # Переход на страницу логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Проверка находится ли элемент на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Проверка исчез ли элемент со страницы
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=0.3).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

    # Проверка нет ли элемента на странице
    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=0.3).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Открытие страницы
    def open(self):
        self.browser.get(self.url)

    # Проверка есть ли на странице ссылка на логин
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # функция для решения задачки из алерта
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No  alert presented")

        return True

    # Переход на страницу корзины
    def go_to_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket.click()

    # Проверка авторизации юзера
    def should_be_authorized_user(self, timeout=10):
        WebDriverWait(self.browser, timeout, 0.1).until(
            EC.presence_of_element_located(BasePageLocators.USER_ICON),
            message="User icon is not presented, probably unauthorised user"
        )
