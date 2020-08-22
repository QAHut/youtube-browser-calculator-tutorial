*** Settings ***
Resource  resources.robot


*** Keywords ***
Browser Setup
    Open Browser  url=${LANDING_PAGE}  browser=${BROWSER}

Enter Expression And Verify Result
    [Arguments]  @{args}  ${expected}=${EMPTY}
    Enter Expression  @{args}
    Latest Result Should Be  ${expected}

User Entered Expression
    [Arguments]  @{args}
    Enter Expression  @{args}

User Enters Expression
    [Arguments]  @{args}
    Enter Expression  @{args}
