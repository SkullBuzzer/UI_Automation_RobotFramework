*** Comments ***
#######################################################################################
Objective : Aim of the test case is to check the sorting of products
Author: M Gurubasava
#######################################################################################

*** Settings ***
Library    SeleniumLibrary
Library    ../page_objects/login_page.py
Library    ../page_objects/add_to_cart_page.py
Library    ../utils/setup_and_teardown.py

Resource    ../resource/login_page_keywords.robot
Resource    ../resource/add_to_cart_page_keywords.robot

Variables    ../test_data/test_case_data.yaml

Suite Setup    Launch Browser
Suite Teardown    Close Browser Window


*** Variables ***
${EXP_TITLE}    Swag Labs

*** Test Cases ***
Set Selenium Execution Speed :
    Set Selenium Speed    0.3s

Login To Application And Validate Webpage :
    Enter Username    ${USER_CREDENTIALS['username']}
    Enter Password    ${USER_CREDENTIALS['password']}
    Click On Login Button
    Validate Login Page Title    ${EXP_TITLE}

Validate Sorting Of All Products By Name Before Selecting Dropdown :
    ${result} =    Check All Products Are Sorted    sort_by_name=${True}    sort_rev=${False}
    Run Keyword If    not ${result}    Fail    Products are not sorted as expected

Validate Sorting of All Products By Name After Selecting Dropdown :
    Click On Dropdown To Sort Items    1
    ${result} =    Check All Products Are Sorted    sort_by_name=${True}    sort_rev=${True}
    Run Keyword If    not ${result}    Fail    Products are not sorted as expected

Validate Sorting Of All Products By Cost From Low To High :
    Click On Dropdown To Sort Items    2
    ${result} =    Check All Products Are Sorted    sort_by_price=${True}    sort_rev=${False}
    Run Keyword If    not ${result}    Fail    Products are not sorted as expected

Validate Sorting Of All Products By Cost From High To Low :
    Click On Dropdown To Sort Items    3
    ${result} =    Check All Products Are Sorted    sort_by_price=${True}    sort_rev=${True}
    Run Keyword If    not ${result}    Fail    Products are not sorted as expected
