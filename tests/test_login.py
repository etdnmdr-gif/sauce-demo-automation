import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Авторизация")
class TestLogin:
    @allure.title("Успешный логин")
    def test_success_login(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "secret_sauce")
        assert "inventory.html" in page.get_current_url()
    @allure.title("Неверный пароль")
    def test_wrong_password(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "wrong_password")
        assert "Username and password do not match" in page.get_error_text()
    @allure.title("Заблокированный пользователь")
    def test_locked_user(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("locked_out_user", "secret_sauce")
        assert "Sorry, this user has been locked out" in page.get_error_text()
    @allure.title("Пустые поля")
    def test_empty_fields(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("", "")
        assert "Username is required" in page.get_error_text()
    @allure.title("Performance glitch")
    def test_performance_glitch(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("performance_glitch_user", "secret_sauce")
        assert "inventory.html" in page.get_current_url()
