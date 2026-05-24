from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then

from conftest import test_user_data

scenarios("../features/registration_login.feature")

@given("I navigate to the parabank website")
def navigate_to_parabank_website(pages):
    pages.hp.navigate_to_homepage()
    pages.hp.click_register_link()

@when("I click on Register link")
def click_register_link(pages):
    pages.hp.click_register_link()

@when("I fill the registration form with valid data")
def fill_registration_form(pages,test_user_data):
    pages.registration.fill_registration_form(test_user_data)

@when("I submit the registration form")
def submit_registration_form(pages, test_user_data):
    pages.registration.submit_registration()
    print(f"Registration Successful for {test_user_data['username']}")

@when("I logout")
def logout(pages):
    pages.registration.logout()

@when("I navigate to the homepage again")
def navigate_to_homepage_again(pages):
    pages.hp.navigate_to_homepage()

@when("I login with valid user credentials")
def login_with_valid_credentials(pages,test_user_data):
    print(f"Logging in with {test_user_data['username']}")
    pages.hp.login(username=test_user_data['username'], password=test_user_data['password'])

@then("I should be able to see the success message")
def check_successful_registration(pages):
    expect(pages.registration.verify_registration_success()).to_be_visible()

@then("I should be able to check/view my balance")
def check_my_balance(pages):
    balance = pages.login.get_balance()
    print(f"Balance is {balance}")