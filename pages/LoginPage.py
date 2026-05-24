from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.balance = page.locator("#accountTable tbody tr").first.locator("td:nth-child(2)")

    def get_balance(self):
        balance = self.balance.inner_text()
        return balance