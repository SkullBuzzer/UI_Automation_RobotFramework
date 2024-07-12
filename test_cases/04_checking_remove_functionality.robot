*** Comments ***
######################################################################
Objective:- The Aim of the test case to check the Remove functionality
Author:- Gurubasava M
######################################################################


*** Settings ***
Library    SeleniumLibrary    run_on_failure=Nothing
Library    ../utils/setup_and_teardown.py
Library    ../page_objects/login_page.py
Library    ../page_objects/add_to_cart_page.py

Resource    ../resource/login_page_keywords.robot
Resource    ../resource/add_to_cart_page_keywords.robot

Variables    ../test_data/test_case_data.yaml
Variables    ../page_objects/add_to_cart_page.py

Suite Setup    Launch Browser
Suite Teardown    Close Browser Window

*** Variables ***
${EXP_TITLE}    Swag Labs
${NO_ITEMS_BFR_REMOVE}    ${1}
${EXP_BTN1}    Remove
${EXP_BTN2}    Add to cart


*** Test Cases ***
Set Selenium Execution Speed :
    Set Selenium Speed    0.3s

Login To Application And Validate Webpage :
    Enter Username    ${USER_CREDENTIALS['username']}
    Enter Password    ${USER_CREDENTIALS['password']}
    Click On Login Button
    Validate Login Page Title    ${EXP_TITLE}

Check Remove Functionality By Adding Product To Cart :
    Add Req Item To Cart    ${PRODUCT_DETALS['product_name']}
    Validate Remove Functionality    ${NO_ITEMS_BFR_REMOVE}    ${EXP_BTN1}    ${EXP_BTN2}

Remove Item From Cart Page And Validate The Added Item :
    Add Req Item To Cart    ${PRODUCT_DETALS['product_name']}
    Click On Shipping Cart Link
    Click Element    xpath://button[@id='remove-sauce-labs-backpack']
    Element Should Not Be Visible    xpath://button[@id='remove-sauce-labs-backpack']
