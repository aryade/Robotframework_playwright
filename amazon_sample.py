from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.amazon.in")
    searchtextbox = page.click('#Search Amazon.in')
    searchtextbox.type('mobile')
    page.click("nav-search-submit-button")

    page.wait_for_timeout(3000)
    browser.close()