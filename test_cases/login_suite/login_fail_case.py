import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from common import login
from selenium.webdriver.support.wait import WebDriverWait
from common import set_driver
# from conf.conf_until import read_config

current_path = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current_path, '../../webdriver/chromedriver.exe')
class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:
        # a=read_config.read('default','URL')
        # print(type(a),a)
        self.driver=set_driver.set_driver()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_Login_fail(self):
        '''case03 使用test01帐号 测试是否能登录'''
        login.login(self.driver,'test01','Aa21281991')
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present()))
        # a=WebDriverWait(self.driver,10).until(EC.alert_is_present())
        # print(a)


if __name__=='__main__':
    unittest.main( verbosity=2)
