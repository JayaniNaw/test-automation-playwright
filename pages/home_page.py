from playwright.sync_api import Page

class HomePage:
    
    # Initialise the page object with a Playwright browser tab.
    # Page = Playwright’s type representing a browser tab
    # __init__ runs when you create a HomePage object:
    #It stores the browser page and locator on that object:
    #self is oject of HomePage 
    def __init__(self, page: Page): 
        # Store the browser tab in an attribute named page on this HomePage object.
        self.page = page
    
        #Locators
        #Docs link element
        #self.doc_link makes the locator available to other methods in the same object.
        self.doc_link = page.get_by_role("link", name = "Docs", exact= True)
        #page.locator["//a[@href = '/docs/intro']"]
        
        self.get_started_btn = page.get_by_role("link", name = "Get started", exact = True)
 

    #Actions
    #click 'Doc' link
    def click_doc_link(self):
        self.doc_link.click()