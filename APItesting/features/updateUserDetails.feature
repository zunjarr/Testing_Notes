Feature: Update the details of user

  Scenario: Verify updated details of user
    Given Provided data to update info of user
    When Run the put method
    Then Verify updated data of user