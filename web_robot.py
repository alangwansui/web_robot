from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class Web_Robot(webdriver.Firefox):
    def send_key(self, id_name, value, type='name'):
        if type=='id':
            elem = self.find_element_by_id(id_name) # Find the query box    
        if type=='name':
            elem = self.find_element_by_name(id_name) # Find the query box    
        elem.send_keys(value)
    def click_button(self, class_name='' ):
        bt = self.find_element_by_class_name(class_name)
        bt.click()