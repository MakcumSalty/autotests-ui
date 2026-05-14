from playwright.sync_api import sync_playwright, expect
import pytest

from fixtures.pages import dashboard_page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):  # Создаем тестовую функцию

    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email="email", username="username", password="password")
    registration_page.click_registration_button()

    dashboard_page.check_visible_dashboard_title()



    # # Все остальные действия остаются без изменений
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #
    #     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    #
    #     email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    #     email_input.fill('user@gmail.com')
    #
    #     username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    #     username_input.fill('username')
    #
    #     password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    #     password_input.fill('password')
    #
    #     registration_button = page.get_by_test_id('registration-page-registration-button')
    #     registration_button.click()
    #
    #     context.storage_state(path='browser-state.json')
    #
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state='browser-state.json')
    #     page = context.new_page()
    #
    #     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    #
    #     page.wait_for_timeout(5000)