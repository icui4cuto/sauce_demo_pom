from base.base_test import BaseTest
from pages.cart_page import CartPage
from pages.overview_page import OverviewPage
from pages.your_information_page import YourInformationPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestSmoke(BaseTest):
    def test_buy_product(self):
        """ Проверка возможности авторизации, добавления товара в корзину, заполнения данных и завершения заказа"""

        # Авторизация
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_user()

        # Выбор товара, добавление в корзину и получение информации о нем
        main_page = MainPage(self.driver)
        product_information_on_main_page = main_page.get_product_information_sauce_labs_backpack()
        main_page.add_sauce_labs_backpack_to_cart()

        # Переход в корзину
        main_page.go_to_cart()

        # Получение информации о товаре в корзине
        cart_page = CartPage(self.driver)
        product_information_in_cart = cart_page.get_product_information_sauce_labs_backpack_in_cart()

        # Проверка имени и цены товара на главной странице и в корзине
        self.assertEqual(product_information_on_main_page, product_information_in_cart)

        # Переход на страницу 'your information'
        cart_page.go_to_your_information()

        # Заполняем информацию о клиенте
        your_information_page = YourInformationPage(self.driver)
        your_information_page.enter_client_information()

        # Переход на страницу 'overview'
        your_information_page.go_to_overview()

        # Получение информации о товаре на странице 'overview'
        overview_page = OverviewPage(self.driver)
        product_information_in_overview = overview_page.get_product_information_sauce_labs_backpack_in_overview()

        # Проверка имени и цены товара на главной странице и на странице 'overview'
        self.assertEqual(product_information_on_main_page, product_information_in_overview)

        # Переход на страницу 'finish'
        overview_page.go_to_finish()

        # Проверка успешного заказа
        self.assertIn("checkout-complete", self.driver.current_url)
