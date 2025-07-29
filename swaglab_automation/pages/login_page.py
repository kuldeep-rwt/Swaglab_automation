from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(1)
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)