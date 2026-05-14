from playwright.sync_api import Playwright, Page, expect  # Импорт Playwright для синхронного режима и проверки
import pytest
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password',
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
)
def test_wrong_data_authorization(login_page: LoginPage, email: str, password: str):
    # Переходим на страницу авторизации
    #login_page = LoginPage(page=chromium_page) без фикстуры и плагина pages
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

    """было без РОМ"""
    # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    #
    # # Находим поле "Email" и заполняем его
    # # email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    # email_input = chromium_page.get_by_test_id("login-form-email-input").locator('input')
    # email_input.fill(email)
    #
    # # page.wait_for_timeout(2000)
    #
    # # Находим поле "Password" и заполняем его
    # # password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    # password_input = chromium_page.get_by_test_id("login-form-password-input").locator('input')
    # password_input.fill(password)
    #
    # # page.wait_for_timeout(1000)
    #
    # # Находим кнопку "Login" и кликаем на нее
    # # login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    # login_button = chromium_page.get_by_test_id("login-page-login-button")
    # login_button.click()
    #
    # # Проверяем, что появилось сообщение об ошибке
    # # wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    # wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # expect(wrong_email_or_password_alert).to_be_visible()  # Проверяем видимость элемента
    # expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")  # Проверяем текст
