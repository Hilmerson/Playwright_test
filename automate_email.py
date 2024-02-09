from dotenv import load_dotenv
import os
import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright

load_dotenv()

# Link to the Gherkin feature file for BDD tests
scenarios('email.feature')

@pytest.fixture(scope="session")
def browser():
    # Launches a browser session for the test suite
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)  # Set headless=True for background execution
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    # Creates a fresh browser page for each test function
    page = browser.new_page()
    yield page
    page.close()

@given('the user logs in with correct credentials')
def log_in(page):
    # Login steps to access the email account
    page.goto('https://mail.yahoo.com')
    page.fill('#login-username', os.environ['PLAYWRIGHT_EMAIL_USERNAME'])
    with page.expect_navigation():
        page.keyboard.press('Enter')
    page.fill('#login-passwd', os.environ['PLAYWRIGHT_EMAIL_PASSWORD'])
    with page.expect_navigation():
        page.keyboard.press('Enter')

@then('the user should see the inbox')
def verify_inbox_page(page):
    # Verifies that the user has successfully navigated to the inbox after login
    assert 'https://mail.yahoo.com/d/folders/' in page.url, "Inbox URL is not in the current URL"

@when('the user creates an email from contacts and adds an attachment')
def create_and_send_email(page):
    # Composes an email from contacts, adds an attachment, and sends the email
    page.click('a[data-test-id="compose-button"]')
    page.click('#to')
    page.wait_for_selector('[data-test-id="contact-item"]', state='attached')
    contact_items = page.query_selector_all('[data-test-id="contact-item"]')
    if len(contact_items) > 1:
        contact_items[1].click()  # Selects the second contact item
    page.click('button[data-test-id="done"]')
    page.fill('[data-test-id="compose-subject"]', 'This is a test of automating emails')
    page.set_input_files('input[type="file"]', 'Hilmer_CV.pdf')
    page.click('[data-test-id="rte"]')
    page.type('[data-test-id="rte"]', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi facilisis viverra cursus. Quisque id elit ut mauris congue placerat ut in ex. Donec semper lacinia dui vel mattis. In hac habitasse platea dictumst. Donec id imperdiet eros. Nam sagittis est eget imperdiet congue. Nullam non porta odio. Nam eget tempus est. Suspendisse sodales tincidunt nunc, vitae maximus est ultricies aliquet. Donec et velit eros. Nulla facilisi. Donec vel tempor tellus, vel sodales augue. Donec scelerisque sapien ligula, non luctus nisi mattis id.')
    with page.expect_navigation():
        page.click('button[data-test-id="compose-send-button"]')

@then('the email with the attachment should be successfully sent')
def verify_email_sent(page):
    # Placeholder for validating successful email send. Adjust validation as needed.
    assert 'https://mail.yahoo.com/d/folders/' in page.url, "There was an error sending the message."

@when('the user logs out')
def log_out(page):
    # Logs out from the email account
    page.hover('#ybarAccountMenuOpener')
    page.click('#profile-signout-link')

@then('the user should see the login page')
def verify_login_page(page):
    # Verifies that the user is redirected to the login page after logout
    assert page.url == 'https://www.yahoo.com/'
