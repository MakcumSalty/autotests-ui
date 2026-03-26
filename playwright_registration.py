from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

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

    # Находим кнопку "Registration" и кликаем на нее
    # registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]]')
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    #header = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')
    header = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(header).to_be_visible()  # Проверяем видимость элемента
    expect(header).to_have_text("Dashboard")  # Проверяем текст

    page.wait_for_timeout(3000)

