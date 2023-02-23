Feature: Verify user is added successfully

  Scenario: Verify add user functionality
    Given User details are provided
    When Run the post method to add user
    Then Verify user added successfully
