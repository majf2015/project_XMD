# -*- coding: utf-8 -*-
from selenium import webdriver
import ConfigParser,sys,os


class Public:
    def __init__(self):
        self.current_path = sys.path[0]
        self.project_path = os.path.dirname(os.path.dirname(self.current_path))
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(os.path.join(self.project_path,'config.conf'))
        self.url = self.conf.get('Url','test_url')
        self.account = dict(self.conf.items('ManagerAccount'))
        self.browser = webdriver.Chrome()
        self.debug = int(self.conf.get('Debug','debug'))
    '''
    #把一些方法变成可读写属性来调用
    @property
    def current_path(self):
        return self.current_path

    @property
    def project_path(self):
        return self.project_path

    @property
    def conf(self):
        return self.conf

    '''


    def login(self):
        self.browser.get(self.url)
        self.browser.find_element_by_id('user-name').send_keys(self.account['user'])
        self.browser.find_element_by_id('user-pw').send_keys(self.account['password'])
        self.browser.find_element_by_xpath("//input[@value= '立即登录']").click()
