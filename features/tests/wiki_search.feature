# Created by Hyun at 4/7/2023
Feature: Test cases for Wiki

  Scenario: User can search on Wikipedia
    Given Skip onboarding
    When Click on search icon
    And Search for Python (programming language)
    Then Verify search result shown for Python (programming language)