#Pytest package is used to write test scripts using Python.
#Install pytest inside the virtual env.

from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.document_page import DocumentPage
import data

# When a test needs that fixture, its parameter name must match the fixture name in conftest.py
# Pytest matches the parameter name to the fixture, runs the fixture, and supplies its result.
def test_doc_navigation(playwright_home:HomePage):
    playwright_home.click_doc_link();
    #create a DocumentPage object using the same browser tab
    document_page = DocumentPage(playwright_home.page)
    
    # Check the navigation succeeded.
    # Check page URL
    expect(playwright_home.page).to_have_url(data.doc_url)
    
    #Check list first title text
    expect(document_page.getting_started).to_have_text('Getting Started')