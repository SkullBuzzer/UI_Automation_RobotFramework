import logging
from robot.libraries.BuiltIn import BuiltIn

class LoginPage:
    USERNAME_FIELD = "id:user-name"
    PASSWORD_FIELD = "name:password"
    LOGIN_BUTTON = "xpath://input[@id='login-button']"
    ERROR_MSG = "xpath://h3[@data-test='error']"
    MENU = "id:react-burger-menu-btn"
    LOGOUT_BTN = "xpath://div[@class='bm-menu']/nav/a[3]"

    def __init__(self, input_un=None, input_pwd=None) -> None:
        self.input_un = input_un
        self.input_pwd = input_pwd
    
    @staticmethod
    def login_page_actions(keywords, *args):
        """ This method can be used to call the diff keywords from robot file """
        return BuiltIn().run_keyword(keywords, *args)

    def enter_un_pwd_and_click_login(self):
        if self.input_un:
            self.login_page_actions("Input Username", self.USERNAME_FIELD, self.input_un)
        elif self.input_pwd:
            self.login_page_actions("Input Password", self.PASSWORD_FIELD, self.input_pwd)
        else:
            self.login_page_actions("Click Login", self.LOGIN_BUTTON)
    
    def get_login_page_title(self):
        act_title = self.login_page_actions("Get Page Title")
        return act_title
    
    def get_error_message(self):
        error_msg = self.login_page_actions("Get Error Msg", self.ERROR_MSG)
        return error_msg

    def option_menu(self):
        self.login_page_actions("Click Element", self.MENU)
        self.login_page_actions("Click Element", self.LOGOUT_BTN)
    
    def un_pwd_enbled(self):
        self.login_page_actions("Check Elements After Logout", self.USERNAME_FIELD, self.PASSWORD_FIELD)

####################################################################
# Python functions to perform action on the login page and validate
####################################################################

def enter_username(input_username):
    """ This method can be used to enter user name in the text box """
    req_login_page = LoginPage(input_un=input_username)
    req_login_page.enter_un_pwd_and_click_login()

def enter_password(input_password):
    """ This method can be used to enter password in the text box """
    req_login_page = LoginPage(input_pwd=input_password)
    req_login_page.enter_un_pwd_and_click_login()

def click_on_login_button():
    """ This method can be used to click on login button"""
    req_login_page = LoginPage()
    req_login_page.enter_un_pwd_and_click_login()

def validate_login_page_title(exp_title):
    """ This method can be used to get the login page title """
    req_login_page = LoginPage()
    act_title = req_login_page.get_login_page_title()
    assert act_title == exp_title, "Expected page not found expected page is "+exp_title+" but found "+act_title

def validate_error_message(exp_error):
    """ This method can be used to validate the error message """
    req_login_page = LoginPage()
    act_error = req_login_page.get_error_message()
    assert act_error == exp_error, "Error Message doesn't match"

def click_on_logout_button():
    """ This method can be used to loogout application """
    req_login_page = LoginPage()
    req_login_page.option_menu()

def validate_un_pwd_page_aftr_logout():
    """ This method can be used to validate the page after logout"""
    req_login_page = LoginPage()
    req_login_page.un_pwd_enbled()
