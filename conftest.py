
from playwright.sync_api import Page
from pages.home_page import HomePage
import pytest
import data

@pytest.fixture
def playwright_home(page:Page):
    # Open the website in the browser tab.
    page.goto(data.url)

    # Create ONE HomePage object using that tab.
    home_page = HomePage(page)

    # Give this object to the test.
    return home_page