Feature: Fetch and verify particular value from parsed JSON format

  Scenario: Verify fetched value from parsed JSON format
    Given Given input details
    When Run get method and parse response to JSON format
    Then Fetch and verify specific value using JSON path