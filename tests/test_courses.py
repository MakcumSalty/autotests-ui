from playwright.sync_api import Playwright, expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка заголовка страницы
    header = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(header).to_be_visible()
    expect(header).to_have_text("Courses")

    # Проверка иконки на странице
    icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    # Проверка текста на странице
    text_1 = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_1).to_be_visible()
    expect(text_1).to_have_text("There is no results")

    # Проверка текста на странице
    text_2 = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_2).to_be_visible()
    expect(text_2).to_have_text("Results from the load test pipeline will be displayed here")
