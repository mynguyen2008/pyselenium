from tests.testcases.test_base import TestBase
from tests.pages.dashboard.login_page import LoginPage
from tests.pages.dashboard.home_page import HomePage

class LoginTest(TestBase):
    
    login_page = LoginPage()
    home_page = HomePage()
    
    def test_login_001(self):
        self.login_page.open_dashboard()
        self.login_page.login("administrator", "")
#         assert self.home_page.is_At() == True
        self.home_page.log_out()
        
        