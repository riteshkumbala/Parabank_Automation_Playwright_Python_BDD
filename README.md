# Parabank Automation
Automated test suite for the Parabank demo banking application (https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC).

Framework: Playwright + Python + pytest-bdd (BDD / Gherkin) + Page Object Model (POM)

---

#  Scenarios Covered

TC_001 - Register a new account with valid data 
TC_002 - Login with valid registered credentials
TC__003 - Account balance printed after login


Full test case documentation is in "Test_Cases.xlsx".

---

# Project Structure

Parabank_Automation/
│
├── pages/                    ← Page Object Model (POM) layer
│   ├── HomePage.py           ← Homepage: navigation + login form
│   ├── LoginPage.py          ← Post-login page: Log the balance
│   └── Registration.py       ← Registration form: all fields + submit + messages
│ 
├── tests/
│   ├── data/
│   │   └── test_data.json             ← Test input data (user details, credentials)
│   └── features/
│       └── registration_login.feature ← BDD scenarios written in plain English (Gherkin syntax)  
│
├── steps/                             ← pytest-bdd step definitions (Gherkin → Python)
│   └── test_registration_login.py     ← @given / @when / @then implementations
│
├── conftest.py                         ← Shared Playwright browser + page fixtures (session-scoped)
├── Test_Cases.xlsx            ← Manual test case documentation
└── README.md


# Design Decisions

Why scope="session" for the browser fixture?
Registration and login are sequential — they share state (the newly created user). Using a session-scoped browser keeps the same context alive across both scenarios, so the registered username is available when the login test runs.

Why random username genaeration for the username?
Parabank is a shared public demo server. If the username is hardcoded, it will likely already exist and the registration test will fail. Using enerate_random_username() generates a unique username on every test run, making it reliably repeatable.

Why headless=False?
This makes the browser visible while running, which is useful for screen recording as proof of execution. Change headless=True for CI pipelines.

---

# Setup and Installation

## Prerequisites
- Python 3.10 or higher
- Git
- PyCharm 

---

##Step 1 — Clone the repository

git clone https://github.com/riteshkumbala/Parabank_Automation_Playwright_Python_BDD.git
cd parabank-automation

---

## Step 2 — Install Python dependencies

pip install -r requirements.txt

---

## Step 3 — Install Playwright browser binaries

playwright install 

This downloads the browser that Playwright controls. You only need to do this once.

---

## Step 4 — Run all tests

pytest

This runs all test scenarios in order:
1. Register new account
2. Login + print balance

---

# Sample Console Output

When tests run, you will see output like this in the terminal:

(.venv) PS C:\Users\RK\PycharmProjects\Parabank_Automation> pytest tests/steps/ -v -s
=============================================================================== test session starts ===============================================================================
platform win32 -- Python 3.14.2, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\RK\PyCharmMiscProject\.venv\Scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.14.2', 'Platform': 'Windows-11-10.0.26200-SP0', 'Packages': {'pytest': '9.0.3', 'pluggy': '1.6.0'}, 'Plugins': {'base-url': '2.1.0', 'bdd': '8.1.0', 'html': '4.2.0', 'metadata': '3.1.1', 'playwright': '0.8.0'}, 'JAVA_HOME': 'C:\\Users\\RK\\scoop\\apps\\temurin21-jdk\\current', 'Base URL': ''}
rootdir: C:\Users\RK\PycharmProjects\Parabank_Automation
plugins: base-url-2.1.0, bdd-8.1.0, html-4.2.0, metadata-3.1.1, playwright-0.8.0
collected 1 item                                                                                                                                                                   

tests/steps/test_registration_login_steps.py::test_registration_and_login Registration Successful for testuser_hqovdca4
Logging in with testuser_hqovdca4
Balance is $515.50
PASSED

================================================================================ 1 passed in 7.43s ================================================================================

---

# Proof of Execution

The video proof is added in proof/ folder

---

# Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Language |
| Playwright | 1.44.0 | Browser automation |
| pytest | 8.2.0 | Test runner |
| pytest-bdd | 7.2.0 | BDD / Gherkin support |
| pytest-playwright | 0.5.0 | Playwright-pytest integration |

---

# Author

Ritesh Kumbala - QA Automation Engineer  
