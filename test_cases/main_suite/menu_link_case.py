import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

current_path = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current_path, '../../webdriver/chromedriver.exe')
class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/zentao/user-login.html?tid=mdjkhgvq')
        self.driver.find_element(By.XPATH, '//input[@class="form-control" and @name="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@class="form-control" and @name="password"]').send_keys('Aa2128199')
        self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary" and @type="submit"]').click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_my_link(self):
        '''case05 点击地盘是否跳转成功'''
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//a[@data-app="my"]').click()
        # time.sleep(2)
        # self.driver.switch_to.frame('appIframe-my')
        self.assertTrue(EC.title_is('地盘 - 禅道'))

    def test_product_link(self):
        '''case04 点击产品是否跳转成功'''
        self.driver.find_element(By.XPATH,'//a[@data-app="product"]').click()
        # self.driver.switch_to.frame('appIframe-product')
        self.assertTrue(EC.title_is('产品 - 禅道'))



if __name__=='__main__':
    unittest.main( verbosity=2)
