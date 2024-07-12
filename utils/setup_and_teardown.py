from robot.libraries.BuiltIn import BuiltIn

class BrowserSetup:
    """ This class can be used to setup the browser """

    SITE_URL = "https://www.saucedemo.com/"
    BROWSER = "chrome"

    def __init__(self) -> None:
        pass

    @staticmethod
    def call_robot_keyword_for_browser_setup(keywords, *args):
        return  BuiltIn().run_keyword(keywords, *args)
    
    def open_browser(self):
        self.call_robot_keyword_for_browser_setup("Open Browser", self.SITE_URL, self.BROWSER)
    
    def maximize_window(self):
        self.call_robot_keyword_for_browser_setup("Maximize Browser Window")
    
    def close_browser_window(self):
        self.call_robot_keyword_for_browser_setup("Close Browser")

#######################################
# python function to setup browser 
#######################################

def launch_browser():
    """ This method can be used to launch and maximize the browser """
    set_browser = BrowserSetup()
    set_browser.open_browser()
    set_browser.maximize_window()

def close_browser_window():
    """ This method can be used to close the  browser """
    set_browser = BrowserSetup()
    set_browser.close_browser_window()
