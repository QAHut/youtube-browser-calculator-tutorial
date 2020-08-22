*** Settings ***
Resource  keywords.robot

Suite Setup  Browser Setup
Suite Teardown  Close Browser


*** Test Cases ***
Templated Test Case
    [Template]  Enter Expression And Verify Result
    (12*3)/(5+1)    enter       expected=6
    5*5             enter       expected=25
    1-1             enter       expected=0
    1-10            enter       expected=-9

Clear All Results
    Results Should Exist
    Clear All
    Results Should Be Cleared

Ans Button Test Case
    Given User Entered Expression  12*3  enter
    When User Enters Expression  ans  *2  enter
    Then Latest Result Should Be  72
