from selenium.webdriver.common.by import By
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self, first, last, postal):
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        time.sleep(1)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        time.sleep(1)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)
        time.sleep(1)
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(2)

    def finish_checkout(self):
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "back-to-products").click()
        time.sleep(2)