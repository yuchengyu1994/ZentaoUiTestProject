import os
from selenium import webdriver



current_path = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')

def set_driver():
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1/zentao/user-login.html?tid=mdjkhgvq')
    return driver