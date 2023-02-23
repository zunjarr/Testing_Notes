Feature: Verification of basic authentication

  Scenario: Verify authentication functionality
    Given Provided user credentials
    When Run the get method
    Then Verify successful authentication