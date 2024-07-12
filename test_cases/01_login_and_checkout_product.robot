*** Comments ***
#######################################################################################
Objective : Aim of the test case is to check the end to end process of product checkout
Author: M Gurubasava
#######################################################################################

*** Settings ***
Library    DateTime
Library    Collections
Library    SeleniumLibrary    run_on_failure=Nothing
Library    ../page_objects/login_page.py
Library    ../page_objects/add_to_cart_page.py
Library    ../page_objects/customer_info_page.py
Library    ../page_objects/order_summary_page.py
Library    ../page_objects/checkout_page.py
Library    ../utils/setup_and_teardown.py

Resource    ../resource/login_page_keywords.robot
Resource    ../resource/add_to_cart_page_keywords.robot
Resource    ../resource/customer_info_keywords.robot
Resource    ../resource/order_summary_keywords.robot
Resource    ../resource/checkout_page_keywords.robot

Variables    ../test_data/test_case_data.yaml

Suite Setup    Launch Browser
Suite Teardown    Close Browser Window

*** Variables ***
${EXP_TITLE}    Swag Labs
${EXP_CART_PAGE}    Your Cart
${EXP_CUST_INFO_PAGE}    Checkout: Your Information
@{EXP_ORD_SUMMARY_PAGES}    Checkout: Overview    Payment Information
${EXP_FINAL_PAGE}    Checkout: Complete!
${EXP_CONF_MESSAGE}    Thank you for your order!


*** Test Cases ***
Set Selenium Execution Speed :
    Set Selenium Speed    0.5s

Login To Application And Validate The Login Page :
    Enter Username    ${USER_CREDENTIALS['username']}
    Enter Password    ${USER_CREDENTIALS['password']}
    Click On Login Button
    Validate Login Page Title    ${EXP_TITLE}

Add Item To the Cart and Validate The Item :
    Add Req Item To Cart    ${PRODUCT_DETALS['product_name']}
    Click On Shipping Cart Link
    Validate Add To Cart Page    ${EXP_CART_PAGE}
    Validate Added Item In Cart Page    ${PRODUCT_DETALS['product_name']}
    
Enter Customer Details and Validate Cust Info Page :
    Click On Checkout Btn
    Validate Cust Info Page    ${EXP_CUST_INFO_PAGE}
    Enter Customer Details    ${CUSTOMER_INFO["first_name"]}    ${CUSTOMER_INFO["last_name"]}    ${CUSTOMER_INFO["postal_code"]}

Click And Validate Order Summary Page :
    Click On Continue Button
    Validate Order Summary Page    ${EXP_ORD_SUMMARY_PAGES}

Place order And Verify The Conf Message :
    Click On Finish Button
    Validate Checkout Page And Conf Message    ${EXP_FINAL_PAGE}    ${EXP_CONF_MESSAGE}
