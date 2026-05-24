from playwright.sync_api import Page

from pages.Registration import Registration


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.register_link = page.get_by_role("link", name = "Register")
        self.username_field = page.locator('input[name="username"]')
        self.password_field = page.locator('input[name="password"]')
        self.login_button = page.get_by_role("button", name = "Log In")

    def navigate_to_homepage(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")

    def click_register_link(self):
       self.register_link.click()

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()