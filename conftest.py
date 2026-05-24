import json
import random
import string

import pytest
from playwright.sync_api import Playwright

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.Registration import Registration

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser, request):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path=f"trace-{request.node.name}.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


def generate_random_username(length=8):
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"testuser_{random_chars}"

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def registration(page):
    return Registration(page)

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def pages(home_page, registration, login_page):
    class Pages:
        def __init__(self, home, reg, login):
            self.hp = home
            self.registration = reg
            self.login = login
    return Pages(home_page, registration, login_page)


@pytest.fixture(scope="session")
def test_user_data():
    with open("tests/data/test_data.json") as f:
        data = json.load(f)
        user = data["users"][0].copy()
        user['username'] = generate_random_username()
        return user
