from playwright.sync_api import sync_playwright,expect

with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

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

    page.wait_for_timeout(2000)

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Указываем файл с сохраненным состоянием
    context = browser.new_context(storage_state="browser-state.json")
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    page.wait_for_timeout(2000)

    #Проверка заголовка страницы
    header = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(header).to_be_visible()
    expect(header).to_have_text("Courses")

    # Проверка иконки на странице
    icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    # Проверка текста на странице
    text_1 = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_1).to_be_visible()
    expect(text_1).to_have_text("There is no results")

    # Проверка текста на странице
    text_2 = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_2).to_be_visible()
    expect(text_2).to_have_text("Results from the load test pipeline will be displayed here")

