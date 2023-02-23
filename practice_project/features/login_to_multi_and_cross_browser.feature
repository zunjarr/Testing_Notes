Feature: Multi browser and cross browser testing

  Scenario: Verify login functionality in multi browser and cross browser parallely
    Given Launch the browsers
    When Read login details from the csv
    Then login_with_chrome_browser
    Then login_with_firefox_browser
    Then Check vpn error
    Then Close the browsers and generate report