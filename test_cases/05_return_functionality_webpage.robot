*** Comments ***
#######################################################################################
Objective:- The  Aim of the test case to check the return functionality in the web page
Author:- Gurubasava M
#######################################################################################


*** Settings ***
Library    SeleniumLibrary
Library    ../utils/setup_and_teardown.py
Library    ../page_objects/login_page.py
Library    ../page_objects/add_to_cart_page.py
Library    ../page_objects/customer_info_page.py

Resource    ../resource/login_page_keywords.robot
Resource    ../resource/add_to_cart_page_keywords.robot
Resource    ../resource/customer_info_keywords.robot

Variables    ../test_data/test_case_data.yaml


Suite Setup    Launch Browser
Suite Teardown    Close Browser Window

*** Variables ***
${EXP_TITLE}    Swag Labs
${EXP_CART_PAGE}    Your Cart


*** Test Cases ***
Set Selenium Execution Speed :
    Set Selenium Speed    0.3s

Login To Application And Validate The Page :
    Enter Username    ${USER_CREDENTIALS['username']}
    Enter Password    ${USER_CREDENTIALS['password']}
    Click On Login Button
    Validate Login Page Title    ${EXP_TITLE}

Add Product To The Cart And Validate The Page :
    Add Req Item To Cart    ${PRODUCT_DETALS['product_name']}
    Click On Shipping Cart Link
    Validate Added Item In Cart Page    ${PRODUCT_DETALS['product_name']}

Click Return And Validate The Page :
    Click Cont Shpng Button
    Validate Login Page Title    ${EXP_TITLE}

Click On Cancel Button From cart Page And Validate Resp Page :
    Click On Shipping Cart Link
    Click On Checkout Btn
    Click Cancel Button
    Validate Add To Cart Page    ${EXP_CART_PAGE}

Click On Cancel Button From Ord Summary Page And Validate Resp Page :
    Click On Checkout Btn
    Enter Customer Details    ${CUSTOMER_INFO['first_name']}    ${CUSTOMER_INFO['last_name']}    ${CUSTOMER_INFO['postal_code']}
    Click Cancel Button
    Validate Login Page Title    ${EXP_TITLE}
