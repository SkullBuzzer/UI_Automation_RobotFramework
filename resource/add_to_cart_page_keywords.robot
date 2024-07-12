# Keywords related to add to cart page

*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Keywords ***
Add Item To Cart
    [Arguments]    ${locator}    ${item}
    Page Should Contain    ${item}
    Click Button    ${locator}

Click Shipping Cart
    [Arguments]    ${locator}
    Click Link    ${locator}

Get Cart Page Title
    [Arguments]    ${locator}
    ${title} =    Get Text    ${locator}
    RETURN    ${title}

Check Added Item
    [Arguments]    ${locator}
    ${item} =    Get Text    ${locator}
    RETURN    ${item}

Get Product Name
    @{prod_name_list}    Create List
    FOR    ${i}    IN RANGE    1    7
        ${item_info} =    Get Text    xpath://div[@class='inventory_list']/div[${i}]/div[2]/div/a/div
        Append To List    ${prod_name_list}    ${item_info}  
    END
    RETURN    ${prod_name_list}

Get Product Price
    @{prod_price_list}    Create List
    FOR    ${i}    IN RANGE    1    7
        ${item_price} =    Get Text     xpath://div[@class='inventory_list']/div[${i}]/div[2]/div[2]/div
        Append To List    ${prod_price_list}    ${item_price}
    END
    RETURN    ${prod_price_list}

Select Dropdown
    [Arguments]    ${locator}    ${index}
    Log    ${index}
    Select From List By Index    ${locator}    ${index}

Remove Button
    [Arguments]    ${locator}
    ${text} =    Get Text    ${locator}
    RETURN    ${text}

Product Count
    [Arguments]    ${locator}
    ${no_of_prod} =    Get Text    ${locator}
    RETURN    ${no_of_prod}

Click Remove Button
    [Arguments]    ${rm_locator}    ${add_loctor}=None
    Click Button    ${rm_locator}
    ${text} =    Get Text    ${add_loctor}
    RETURN    ${text}

Click CONT SHPNG BTN 
    [Arguments]    ${locator}
    Click Button    ${locator}
