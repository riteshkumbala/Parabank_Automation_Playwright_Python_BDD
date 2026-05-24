Feature: User Registration and Login Flow
  As a user
  I want to register and login into my account
  So that I am able to check/view my balance

  Scenario: Registration and Login
    Given I navigate to the parabank website
    When I click on Register link
    And I fill the registration form with valid data
    And I submit the registration form
    Then I should be able to see the success message
    When I logout
    And I navigate to the homepage again
    And I login with valid user credentials
    Then I should be able to check/view my balance
