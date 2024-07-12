""" THis file can be used to define cuatomer info page locators, action methods and validation"""

from robot.libraries.BuiltIn import BuiltIn

class CustomerInfoPage:
    """ This class represents customer info page locators, action methods"""

    CHECKOUT_BTN = "id:checkout"
    CUST_INFO_PAGE = "xpath://span[contains(text(),'Checkout: Your Information')]"
    FIRSTNAME = "id:first-name"
    LASTNAME = "name:lastName"
    POSTAL_CODE = "xpath://input[@id='postal-code']"
    CNL_BTN = "id:cancel"

    def __init__(self, first_name=None, last_name=None, postal_code=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code
    
    @staticmethod
    def customer_info_page_actions(keywords, *args):
        return BuiltIn().run_keyword(keywords, *args)
    
    def click_checkout_btn(self):
        self.customer_info_page_actions("Checkout Button", self.CHECKOUT_BTN)

    def get_cust_info_page(self):
        page = self.customer_info_page_actions("Product Cart Page", self.CUST_INFO_PAGE)
        return page

    def input_cust_details(self):
        self.customer_info_page_actions(
            "Customer Deatils", self.FIRSTNAME, self.LASTNAME, self.POSTAL_CODE, self.first_name, self.last_name, self.postal_code
            )
    
    def cancel_btn(self):
        self.customer_info_page_actions("Checkout Button", self.CNL_BTN)

#######################################################################
# Python functions to perform action on the checkout page and validate
#######################################################################

def click_on_checkout_btn():
    """ This method can be used to click on checkout button """
    cust_info_page = CustomerInfoPage()
    cust_info_page.click_checkout_btn()

def validate_cust_info_page(exp_page):
    """ This method can be used to validate the cust info page """
    cust_info_page = CustomerInfoPage()
    act_page = cust_info_page.get_cust_info_page()
    assert act_page == exp_page, "Expected page not found. expected "+exp_page+" but found "+act_page

def enter_customer_details(first_name, last_name, postal_code):
    """ This method can be used to enter customer details """
    cust_info_page = CustomerInfoPage(first_name, last_name, postal_code)
    cust_info_page.input_cust_details()

def click_cancel_button():
    """ This method can be used to click cancel button from cust info page """
    cust_info_page = CustomerInfoPage()
    cust_info_page.cancel_btn()