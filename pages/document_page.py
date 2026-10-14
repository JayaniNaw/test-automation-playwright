from playwright.sync_api import Page

class DocumentPage:
    def __init__(self,page:Page):
        self.page = page
        
        #Locators
        self.getting_started = page.locator("//span[@title = 'Getting Started']")