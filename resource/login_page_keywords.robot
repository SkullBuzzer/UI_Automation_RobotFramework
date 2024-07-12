*** Settings ***
Library    SeleniumLibrary
Variables    ../page_objects/login_page.py


*** Keywords ***

Input Username
    [Arguments]    ${locator}    ${username}
    Input Text    ${locator}    ${username}

Input Password
    [Arguments]    ${locator}    ${password}
    Input Text    ${locator}    ${password}

Click Login
    [Arguments]    ${locator}
    Click Button    ${locator}

Get Page Title
    ${act_title} =    Get Title
    RETURN    ${act_title}

Get Error Msg
    [Arguments]    ${locator}
    ${error_msg} =    Get Text    ${locator}
    RETURN    ${error_msg}

Check Elements After Logout
    [Arguments]    ${un_locator}    ${pwd_locator}
    Element Should Be Enabled    ${un_locator}
    Element Should Be Enabled    ${pwd_locator}
