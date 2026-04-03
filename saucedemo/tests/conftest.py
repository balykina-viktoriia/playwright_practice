import pytest
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def set_timeout(page: Page):
    page.set_default_timeout(10000)

