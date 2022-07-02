#coding = utf8
import os
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By

current_path = os.path.dirname(__file__)
cfgpath='config.ini'

class ReadConf:
    def __init__(self,conf_path=cfgpath):
        # self.conf_data=configparser.ConfigParser().read(conf_path)
        self.conf_path=conf_path
        self.conf = configparser.ConfigParser()
        self.conf.read(os.path.join(current_path, self.conf_path))

    def read(self,sec,name):
        # conf = configparser.ConfigParser()
        # conf.read(os.path.join(current_path, self.conf_path))
        return self.conf.get(sec,name)
    @property
    def get_excelpath(self):
        return self.read('default','excel_path')
    @property
    def get_urlpath(self):
        return self.read('default','URL_path')

    @property
    def get_logpath(self):
        return os.path.join(current_path,self.read('default', 'log_path'))

# read_config=ReadConf()
if __name__=='__main__':
    read_config = ReadConf()
    # URL_path=read_config.read('default','URL_path')
    # URL_path=read_config.get_urlpath
    # print(URL_path)
    chrome_driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(read_config.get_urlpath)
    driver.find_element(By.XPATH, '//input[@class="form-control" and @name="account"]').send_keys(read_config.read('mail','username'))
    driver.find_element(By.XPATH, '//input[@class="form-control" and @name="password"]').send_keys(read_config.read('mail','password'))
    driver.find_element(By.XPATH, '//button[@class="btn btn-primary" and @type="submit"]').click()

