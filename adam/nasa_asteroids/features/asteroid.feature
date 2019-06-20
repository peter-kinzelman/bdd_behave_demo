Feature: Verify Asteroids

  In order to communicate effectively to the asteroids functionality
  As a development team
  I want to test Onboarding endpoints and make sure its working as expected with UI

  @api
  Scenario: Verify asteroid data
   Given we have called the API
    When the service method is GET
    Then the Response call should be 200
    And the required data should be present
    And the Nasa Jpl Url should have correct format
    And the Absolute Magnitude should be decimal
    And the Estimated Diameter Max should be greater than the Estimated Diameter Min
    And the Estimated Diameters in miles should be the same in meters
    And the Is Potentially Hazardous Asteroid should be boolean
    And the Close Approach Date should exist if the Approach Data exists
    And the Orbiting Body should exist if the Approach Data exists

  @ui
  Scenario: Verify UI data
   Given I have the asteroid API data
    When I am on the asteroid page
    Then the asteroid should have the same data as the API

  @db
  Scenario: Verify asteroid data against database
    Given We have called the API
     When the service method is GET
     Then the response data should match the database data