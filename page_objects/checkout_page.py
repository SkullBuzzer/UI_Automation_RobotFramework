""" This file can be used to define checkout page locators, action methods and validation"""

import logging
from robot.libraries.BuiltIn import BuiltIn

class CheckoutPage:
    """ This class represents checkout page locators, action methods"""

    FINISH_BTN = "id:finish"
    CHECKOUT_PAGE = "xpath://span[contains(text(),'Checkout: Complete!')]"
    CONFIR_MSG = "xpath://h2[contains(text(),'Thank you for your order!')]"

    def __init__(self) -> None:
        pass

    @staticmethod
    def checkout_page_actions(keywords, *args):
        return BuiltIn().run_keyword(keywords, *args)

    def click_finish_button(self):
        self.checkout_page_actions("Click Finish Button", self.FINISH_BTN)
    
    def get_checkout_page(self):
        page = self.checkout_page_actions("Final Checkout Page", self.CHECKOUT_PAGE, self.CONFIR_MSG)
        return page

#######################################################################
# Python functions to perform action on the checkout page and validate
#######################################################################

def click_on_finish_button():
    """ This method can be used to cllick on finish button """
    checkout_page = CheckoutPage()
    checkout_page.click_finish_button()

def validate_checkout_page_and_conf_message(exp_page, exp_conf_msg):
    """ This method can be used to validate page and conf message """
    checkout_page = CheckoutPage()
    act_messages = checkout_page.get_checkout_page()
    logging.info(act_messages)
    assert act_messages[0] == exp_page, "Expected page not found expected page is "+exp_page+" but found "+act_messages[0]
    assert act_messages[1] == exp_conf_msg, "Expected page not found expected page is "+exp_conf_msg+" but found "+act_messages[1]
