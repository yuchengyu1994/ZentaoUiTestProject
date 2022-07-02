import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

current = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current, '../../webdriver/chromedriver.exe')
class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/zentao/user-login.html?tid=mdjkhgvq')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_Login(self):
        '''case01 使用admin帐号 测试是否能登录'''
        self.driver.find_element(By.XPATH, '//input[@class="form-control" and @name="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//input[@class="form-control" and @name="password"]').send_keys('Aa2128199')
        self.driver.find_element(By.XPATH,'//button[@class="btn btn-primary" and @type="submit"]').click()
        # element=self.driver.find_element(By.XPATH,'//a[@data-app="my"]/span[@class="text"]')
        # self.assertEqual(WebDriverWait(self.driver,10).until(element),'地盘','test_Login执行失败')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//a[@data-app="my"]/span[@class="text"]'),'地盘'))
        time.sleep(2)
    def test_Login01(self):
        '''case02 使用test01帐号 测试是否能登录'''
        self.driver.find_element(By.XPATH, '//input[@class="form-control" and @name="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@class="form-control" and @name="password"]').send_keys('Aa2128199')
        self.driver.find_element(By.XPATH,'//button[@class="btn btn-primary" and @type="submit"]').click()
        element=self.driver.find_element(By.XPATH,'//a[@data-app="my"]/span[@class="text"]')
        self.assertEqual(element.text,'地盘','test_Login执行失败')
        time.sleep(2)

if __name__=='__main__':
    unittest.main( verbosity=2)