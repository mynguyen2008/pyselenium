from selenpy.support import browser
from selenpy.element.text_box import TextBox
from selenpy.element.base_element import BaseElement

class LoginPage():
    
    _txt_username = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("class=btn-login")

    def __init__(self):
        pass
    
    def open_dashboard(self):
        browser.open_url("http://192.168.188.99/TADashboard/login.jsp")
        
    def login(self,username,password):
        self._txt_username.send_keys(username)
        self._txt_password.send_keys(password)
        self._btn_login.click()
        
