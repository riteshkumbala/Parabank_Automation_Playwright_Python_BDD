from playwright.sync_api import expect

def test_registration_login(page, test_user_data, pages):
    print("Starting registration")
    hp = pages.hp
    registration = pages.registration
    login = pages.login
    hp.navigate_to_homepage()
    hp.click_register_link()
    register = registration
    register.fill_registration_form(test_user_data)
    register.submit_registration()
    expect(register.verify_registration_success()).to_be_visible()
    register.logout()
    print(f"Registration Successful for {test_user_data['username']}")
    print(f"Logging in with {test_user_data['username']}")
    hp.navigate_to_homepage()
    hp.login(username=test_user_data['username'], password=test_user_data['password'])
    print("Login successful")
    balance = login.get_balance()
    print(f"Balance = {balance}")
    register.logout()