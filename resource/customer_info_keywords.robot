*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Checkout Button
    [Arguments]    ${locator}
    Click Button    ${locator}

Product Cart Page
    [Arguments]    ${locator}
    ${act_page} =    Get Text    ${locator}
    RETURN    ${act_page}

Customer Deatils
    [Arguments]    ${firstname_loc}    ${lastname_loc}    ${postal_code_loc}    ${firstname}    ${lastname}    ${postal_code}
    Input Text    ${first_name_loc}    ${firstname}   
    Input Text    ${lastname_loc}    ${lastname}
    Input Text    ${postal_code_loc}    ${postal_code}
