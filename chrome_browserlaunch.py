from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto('https://www.google.com/')
        print ('Chrome successfully opened')
        print (page.title())
        page.wait_for_timeout(3000)
        browser.close()

test_google_search()