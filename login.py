# -*- coding: utf-8 -*-
from selenium import webdriver
import global_attributes

class Login:
    def __init__(self):
        self.url =global_attributes.url
        self.account = global_attributes.manager_account
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get(self.url)
        self.browser.find_element_by_id('user-name').send_keys(self.account[0])
        self.browser.find_element_by_id('user-pw').send_keys(self.account[1])
        self.browser.find_element_by_xpath("//input[@value= '立即登录']").click()



