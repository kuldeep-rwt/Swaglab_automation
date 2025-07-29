import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")
    time.sleep(1)
    inventory.add_to_cart()
    time.sleep(1)
    inventory.go_to_cart()
    time.sleep(1)
    checkout.checkout("Aman", "Rathore", "1234321")
    time.sleep(1)
    checkout.finish_checkout()
    time.sleep(1)