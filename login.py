# -*- coding: utf-8 -*-
from selenium import webdriver
import global_attributes

class Login:
    def __init__(self):
        self.url = 'http://192.168.1.100:9880/spa-manager/login'
        self.user_name = u'曲奇'
        self.pass_wd = 'a123456'
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get(self.url)
        self.browser.find_element_by_id('user-name').send_keys(self.user_name)
        self.browser.find_element_by_id('user-pw').send_keys(self.pass_wd)
        self.browser.find_element_by_xpath("//input[@value= '立即登录']").click()

        if global_attributes.debug:
            print self.browser


