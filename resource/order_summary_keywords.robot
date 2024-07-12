# Keywords related to order summmary page

*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Click Continue
    [Arguments]    ${locator}
    Click Button    ${locator}

Order Summary Page
    [Arguments]    ${title_locator}    ${payment_info_loc}
    ${title} =    Get Text    ${title_locator}
    ${payment_info} =    Get Text    ${payment_info_loc}
    RETURN    ${title}    ${payment_info}
