*** Comments ***
#######################################################################################
Objective:- The  Aim of the test case to check the logout functionality of the web page
Author:- Gurubasava M
#######################################################################################


*** Settings ***
Library    SeleniumLibrary
Library    ../utils/setup_and_teardown.py
Library    ../page_objects/login_page.py

Resource    ../resource/login_page_keywords.robot

Variables    ../test_data/test_case_data.yaml

Suite Setup    Launch Browser
Suite Teardown    Close Browser Window

*** Variables ***
${EXP_TITLE}    Swag Labs


*** Test Cases ***
Set Selenium Execution Speed :
    Set Selenium Speed    0.3s

Login To Application And Validate The Page :
    Enter Username    ${USER_CREDENTIALS['username']}
    Enter Password    ${USER_CREDENTIALS['password']}
    Click On Login Button
    Validate Login Page Title    ${EXP_TITLE}

Click On Logout And Validate Resp Page :
    Click On Logout Button
    Validate Un Pwd Page Aftr Logout
