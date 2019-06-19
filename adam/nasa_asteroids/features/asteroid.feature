Feature: Verify Asteroids

  In order to communicate effectively to the asteroids functionality
  As a development team
  I want to test Onboarding endpoints and make sure its working as expected with UI

  Scenario: Verify asteroid data
   Given we have called the api
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

  Scenario: Verify UI data
   Given I am on the asteroid web page
    When I am on the asteroid page
    Then the asteroid should have the same data as the API