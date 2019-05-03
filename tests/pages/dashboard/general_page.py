from selenpy.element.base_element import BaseElement
from selenpy.common import common


class GeneralPage():
    
    _lbl_dashboard = BaseElement("id=header")
    _lbl_user_menu = BaseElement("//a[@href='#Welcome']")
    
    def __init__(self):
        pass
    
    def log_out(self):
        common.move_to(self._lbl_user_menu)