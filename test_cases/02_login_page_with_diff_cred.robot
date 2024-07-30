##############################################################################################
Objective : Aim of the test case is to check the login functionlity with different credentials
Author: M Gurubasava
###############################################################################################

*** Settings ***
Library    SeleniumLibrary
Library    ../utils/setup_and_teardown.py
Library    ../page_objects/login_page.py
Library    DataDriver    C:\ProgramData\Jenkins\.jenkins\workspace\UI_Automation_RobotFramework_Pipeline\test_data    Sheet1

Resource    ../resource/login_page_keywords.robot
Variables    ../test_data/test_case_data.yaml
Test Template    Check Login Function With Invalid Cred

Suite Setup    Launch Browser
Suite Teardown    Close Browser Window

*** Variables ***
${EXP_ERROR}    Epic sadface: Username and password do not match any user in this service

*** Test Cases ***
LoginTestWithExcel using     ${username}    ${password}

*** Keywords ***
Check Login Function With Invalid Cred
    [Arguments]    ${username}    ${password}
    Set Selenium Speed    0.5s
    Enter Username    ${username}
    Enter Password    ${password}
    Click On Login Button
    Validate Error Message    ${EXP_ERROR}
