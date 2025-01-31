*** Settings ***
Resource    digi.resource

*** Test Cases ***

Scenario: Verify Digikala API Returns Valid Response
    Given Setup Digikala API Session
    When Send GET Request To Digikala API
    Then Response Should Be 200
    And Log Response Body
