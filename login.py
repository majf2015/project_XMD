# -*- coding: utf-8 -*-
from selenium import webdriver
import ConfigParser,sys,os


class Login:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/config.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.url = self.conf.get('Url','test_url')
        self.account = dict(self.conf.items('ManagerAccount'))
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get(self.url)
        self.browser.find_element_by_id('user-name').send_keys(self.account['user'])
        self.browser.find_element_by_id('user-pw').send_keys(self.account['password'])
        self.browser.find_element_by_xpath("//input[@value= '立即登录']").click()