
Feature: Verify Stocks

In order to communicate effectively to the Stocks functionality
As a development team
I want to test Onboarding endpoints and make sure its working as expected with UI

  @api
  Scenario: Verify stocks data
   Given we have called the api
    When the service method is GET
    Then the Response call should be 200
    And the required data should be present
    And the symbol should be a unicode
    And the price should be a decimal

  @ui
  Scenario: Verify web page against UI
   Given I am on the yahoo web page
    When I am on the company page
    Then the page should have the same data as the API
