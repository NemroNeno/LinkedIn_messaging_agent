# save_login.py
from playwright.sync_api import sync_playwright

EMAIL = "mnabeel.bese22seecs@seecs.edu.pk"
PASSWORD = "11601409Jedi@"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    ctx = browser.new_context()
    page = ctx.new_page()
    
    page.goto("https://www.linkedin.com/login")
    page.fill("input[name='session_key']", EMAIL)
    page.fill("input[name='session_password']", PASSWORD)
    page.click("button[type='submit']")
    
    try:
        # Wait for the network to be idle and for post-login UI
        page.wait_for_load_state("networkidle", timeout=600000)
        feed_locator = page.locator("div[id*='feed']", has_text="Start a post")
        
        # Ensure the post feed area is visible
        feed_locator.wait_for(state="visible", timeout=60000)
    except TimeoutError:
        print("❌ Login failed or LinkedIn UI structure changed.")
        browser.close()
        exit(1)
    
    ctx.storage_state(path="linkedin_auth.json")
    print("✅ Logged in and storage state saved.")
    browser.close()