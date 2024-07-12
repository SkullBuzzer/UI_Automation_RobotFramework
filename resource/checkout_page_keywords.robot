# Keywords related to order checkout page

*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Click Finish Button
    [Arguments]    ${locator}
    Click Button    ${locator}

Final Checkout Page
    [Arguments]    ${page_locator}    ${conf_message_locator}
    ${page} =     Get Text    ${page_locator}
    ${conf_message} =    Get Text    ${conf_message_locator}
    RETURN    ${page}    ${conf_message}