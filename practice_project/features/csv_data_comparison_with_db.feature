Feature: Compare the csv data against database

  Scenario: Verify ecs_qs column data as well as its respective columns data from csv against database
    Given Read csv data and data from database
    When Check the data for combination of week,channel and prod_grp_id with DB data for all the respective columns whether its same or different
    Then If there is a mismatch in ecs_qs in 4 weeks or outside of 4 weeks is failure
    And If there is a mismatch in any channel other then Pharmacy Retailer, its a failure
    And If there is a mismatch in parameters other then ecs_qs within 4 weeks is pass case
    And Generate the report