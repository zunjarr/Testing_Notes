Feature: Verification of session management

  Scenario: Verify session management functionality
    Given Provided credentials
    When Running get method
    Then Verify response during the session