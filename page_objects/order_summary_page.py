""" This file can be used to define order summary page locators, action methods and validation """

from robot.libraries.BuiltIn import BuiltIn

class OrderSummaryPage:
    """ This class represents order summary page locators, action methods """

    CONTINUE_BTN = "id:continue"
    SUMMARY_PAGE = "xpath://span[contains(text(),'Checkout: Overview')]"
    PAYMENT_INFO = "xpath://div[text()='Payment Information']"

    def __init__(self) -> None:
        pass

    @staticmethod
    def order_summary_page_actions(keywords, *args):
        return BuiltIn().run_keyword(keywords, *args)

    def click_cont_btn(self):
        self.order_summary_page_actions("Click Continue", self.CONTINUE_BTN)

    def get_ord_summary_page(self):
        page = self.order_summary_page_actions("Order Summary Page", self.SUMMARY_PAGE, self.PAYMENT_INFO)
        return page

############################################################################
# Python functions to perform action on the order summary page and validate
############################################################################

def click_on_continue_button():
    """ This method can be used to click on continue button """
    order_summary = OrderSummaryPage()
    order_summary.click_cont_btn()

def validate_order_summary_page(expected_pages):
    """ This method can be used to validate order summary page """
    order_summary = OrderSummaryPage()
    act_pages = order_summary.get_ord_summary_page()
    assert act_pages == expected_pages, "Expected page not found expected page is "+expected_pages+" but found "+act_pages
