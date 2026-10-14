from playwright.sync_api import Page

class HomePage:
    
    # Initialise the page object with a Playwright browser tab.
    #self is oject of HomePage 
    def __init__(self, page: Page): 
        # Store the browser tab in an attribute named page on this HomePage object.
        self.page = page
    
        #Locators
        #Docs link element
        self.doc_link = page.get_by_role("link", name = "Docs", exact= True)
        #page.locator["//a[@href = '/docs/intro']"]
 

    #Actions
    #click 'Doc' link
    def click_doc_link(self):
        self.doc_link.click()