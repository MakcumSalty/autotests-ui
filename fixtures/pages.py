import pytest

from fixtures.browsers import chromium_page
from pages.login_page import LoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)