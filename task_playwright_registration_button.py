from playwright.sync_api import sync_playwright, expect


# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #Проверяем что кнопка "registration" неактивна
    reg_link = page.get_by_test_id("registration-page-registration-button")
    expect(reg_link).to_be_disabled()

    # Находим поле "Email" и заполняем его
    # email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "Username" и заполняем его
    # username_input = page.locator('//div[ @ data - testid = "registration-form-username-input"] // div // input')
    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    # password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    page.wait_for_timeout(2000)

    # Проверяем что кнопка "registration" активна
    expect(reg_link).to_be_enabled()

