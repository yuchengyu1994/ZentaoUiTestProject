from selenium.webdriver.common.by import By


def login(driver,username,passwd):
    driver.find_element(By.XPATH, '//input[@class="form-control" and @name="account"]').send_keys(username)
    driver.find_element(By.XPATH, '//input[@class="form-control" and @name="password"]').send_keys(passwd)
    driver.find_element(By.XPATH, '//button[@class="btn btn-primary" and @type="submit"]').click()