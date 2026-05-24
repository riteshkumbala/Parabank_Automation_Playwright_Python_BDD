from playwright.sync_api import Page


class Registration:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator('[id="customer.firstName"]')
        self.last_name = page.locator('[id="customer.lastName"]')
        self.address = page.locator('[id="customer.address.street"]')
        self.city = page.locator('[id="customer.address.city"]')
        self.state = page.locator('[id="customer.address.state"]')
        self.zip_code = page.locator('[id="customer.address.zipCode"]')
        self.phone = page.locator('[id="customer.phoneNumber"]')
        self.ssn = page.locator('[id="customer.ssn"]')
        self.username = page.locator('[id="customer.username"]')
        self.password = page.locator('[id="customer.password"]')
        self.confirm_password = page.locator('[id="repeatedPassword"]')
        self.register_button = page.get_by_role("button", name = "Register")
        self.logout_button = page.get_by_role("link", name = "Log Out")
        self.success_message = page.get_by_text("Your account was created successfully. You are now logged in.")

    def fill_registration_form(self, user_data):
        self.first_name.fill(user_data["first_name"])
        self.last_name.fill(user_data["last_name"])
        self.address.fill(user_data["address"])
        self.city.fill(user_data["city"])
        self.state.fill(user_data["state"])
        self.zip_code.fill(user_data["zip_code"])
        self.phone.fill(user_data["phone"])
        self.ssn.fill(user_data["ssn"])
        self.username.fill(user_data["username"])
        self.password.fill(user_data["password"])
        self.confirm_password.fill(user_data["password"])

    def submit_registration(self):
        self.register_button.click()

    def verify_registration_success(self):
        return self.success_message

    def logout(self):
        self.logout_button.click()
