from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/')

    # for using with CSS sector: id/ class /attributes
#using id
    emailtextbox = page.wait_for_selector('#email')
    emailtextbox.type('test@gamil.com')
    loginbutton = page.wait_for_selector('#enterimg')
    loginbutton.click()
    page.wait_for_timeout(3000)
    browser.close()
