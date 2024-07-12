""" This file contains locators and actions and validations related to add to cart web page """

import logging
from robot.libraries.BuiltIn import BuiltIn

class AddToCartPage:
    """ This class defines the locators and functions related add to cart page"""

    ADD_TO_CART_BTN = "xpath://button[@id='add-to-cart-sauce-labs-backpack']"
    SHIPPING_CART_LINK = "xpath://a[@class='shopping_cart_link']"
    CART_PAGE = "xpath://span[contains(text(),'Your Cart')]"
    ADDED_PROD = "xpath://div[text()='Sauce Labs Backpack']"
    DROPDOWN = "xpath://select[@class='product_sort_container']"
    REMOVE_BTN = "xpath://button[@id='remove-sauce-labs-backpack']"
    PROD_COUNT = "xpath://span[contains(text(),'1')]"
    CONT_SHOPPING_BTN = "id:continue-shopping"

    def __init__(self, product = None, index = None) -> None:
        self.product = product
        self.index = index
    
    @staticmethod
    def add_to_cart_page_actions(keywords, *args):
        return BuiltIn().run_keyword(keywords, *args)
    
    def add_product_to_cart(self):
        self.add_to_cart_page_actions("Add Item To Cart", self.ADD_TO_CART_BTN, self.product)
        
    def shopping_cart_link(self):
        self.add_to_cart_page_actions("Click Shipping Cart", self.SHIPPING_CART_LINK)

    def get_cart_page_title(self):
        page = self.add_to_cart_page_actions("Get Cart Page Title", self.CART_PAGE)
        return page

    def get_added_item_in_cart_page(self):
        act_item = self.add_to_cart_page_actions("Check Added Item", self.ADDED_PROD)
        return act_item
    
    def get_all_products_name(self):
        all_items_name = self.add_to_cart_page_actions("Get Product Name")
        return all_items_name

    def get_all_products_cost(self):
        all_items_price = self.add_to_cart_page_actions("Get Product Price")
        return all_items_price

    def select_dropdown(self):
        self.add_to_cart_page_actions("Select Dropdown", self.DROPDOWN, self.index)
    
    def no_of_item_before_remove(self):
        text = self.add_to_cart_page_actions("Remove Button", self.REMOVE_BTN)
        no_of_prods = self.add_to_cart_page_actions("Product Count", self.PROD_COUNT)
        return text, no_of_prods

    def no_of_item_after_remove(self):
        text = self.add_to_cart_page_actions("Click Remove Button", self.REMOVE_BTN, self.ADD_TO_CART_BTN)
        return text
    
    def cont_shopng_btn(self):
        self.add_to_cart_page_actions("Click CONT SHPNG BTN ", self.CONT_SHOPPING_BTN)

####################################################################
# Python functions to perform action on the add to cart page and validate
####################################################################

def add_req_item_to_cart(product_to_add):
    """ This method can be used to add the req item to cart """
    req_add_to_cart_page = AddToCartPage(product_to_add)
    req_add_to_cart_page.add_product_to_cart()

def click_on_shipping_cart_link():
    """ This method can be used to click on shipping cart link """
    req_add_to_cart_page = AddToCartPage()
    req_add_to_cart_page.shopping_cart_link()

def validate_add_to_cart_page(exp_page):
    """ This Method can be used to validate the webpage """
    req_add_to_cart_page = AddToCartPage()
    act_page = req_add_to_cart_page.get_cart_page_title()
    assert act_page == exp_page, "Expected page not found. Expected "+exp_page+" but found"+act_page

def validate_added_item_in_cart_page(exp_item):
    """ This method can be used to validate the item added in cart page """
    req_add_to_cart_page = AddToCartPage(exp_item)
    act_item = req_add_to_cart_page.get_added_item_in_cart_page()
    assert act_item == exp_item, "Expected item not found. expected "+exp_item+" but found "+act_item

def click_on_dropdown_to_sort_items(index:str):
    """ This method can be used to select the sortinng dropdown """
    req_add_to_cart_page = AddToCartPage(index=index)
    req_add_to_cart_page.select_dropdown()

def check_all_products_are_sorted(sort_by_name=None, sort_by_price=None, sort_rev=None):
    """ This Method can be used to check all products are sorted """
    req_add_to_cart_page = AddToCartPage()
    if sort_by_name:
        all_prods_name = req_add_to_cart_page.get_all_products_name()
        if sort_rev == False:
            return all_prods_name == sorted(all_prods_name)
        else:
            return all_prods_name == sorted(all_prods_name, reverse=True)
    elif sort_by_price:
        all_prods_price = req_add_to_cart_page.get_all_products_cost()
        all_prod_price_float = []
        for price in all_prods_price:
            price_num = price.replace("$", "")
            all_prod_price_float.append(float(price_num))
        if sort_rev == False:
            return all_prod_price_float == sorted(all_prod_price_float)
        else:
            return all_prod_price_float == sorted(all_prod_price_float, reverse=True)

def validate_remove_functionality(no_of_items_bfr_rem:int, exp_button1, exp_button2):
    """ This method can be used to check the remove functionlity """
    req_add_to_cart_page = AddToCartPage()
    text, prod_count = req_add_to_cart_page.no_of_item_before_remove()
    assert int(prod_count) == no_of_items_bfr_rem, "No of products doesn't match"
    assert text == exp_button1, "Expected button not found"
    text1 = req_add_to_cart_page.no_of_item_after_remove()
    assert text1 == exp_button2, "Expected button not found"

def click_cont_shpng_button():
    """ This Method can be used to click and return button """
    req_add_to_cart_page = AddToCartPage()
    req_add_to_cart_page.cont_shopng_btn()