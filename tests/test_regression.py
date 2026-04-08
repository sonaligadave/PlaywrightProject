import pytest
from config.settings import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.api_client import APIClient
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage



def test_full_checkout_flow(page):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Login
    login_page.load()
    login_page.login_with_credentials(Config.USERNAME,Config.PASSWORD)

    # Add / Remove Products
    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.remove_product("sauce-labs-backpack")

    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.add_product("sauce-labs-bike-light")
    inventory_page.add_product("sauce-labs-bolt-t-shirt")
    inventory_page.add_product("sauce-labs-fleece-jacket")

    inventory_page.remove_product("sauce-labs-bike-light")
    inventory_page.remove_product("sauce-labs-backpack")

    # Go to cart
    inventory_page.open_cart()

    cart_page.verify_product_present("Sauce Labs Fleece Jacket")
    cart_page.continue_shopping()

    # Add more
    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page.remove_product("sauce-labs-bolt-t-shirt")

    # Checkout
    cart_page.checkout()

    checkout_page.fill_information("test", "test", "94335")
    checkout_page.continue_checkout()
    checkout_page.verify_overview_page()

    checkout_page.finish()
    checkout_page.verify_order_complete()


def test_add_single_product(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.load()
    login.login_with_credentials(Config.USERNAME,Config.PASSWORD)

    inventory.add_product("sauce-labs-backpack")
    inventory.verify_product_added("sauce-labs-backpack")


def test_remove_product(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.load()
    login.login_with_credentials(Config.USERNAME,Config.PASSWORD)


    inventory.add_product("sauce-labs-backpack")
    inventory.remove_product("sauce-labs-backpack")
    inventory.verify_product_removed("sauce-labs-backpack")

def test_remove_product(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.load()
    login.login_with_credentials(Config.USERNAME,Config.PASSWORD)

    inventory.add_product("sauce-labs-backpack")
    inventory.remove_product("sauce-labs-backpack")
    inventory.verify_product_removed("sauce-labs-backpack")


def test_add_multiple_products(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.load()
    login.login_with_credentials(Config.USERNAME,Config.PASSWORD)

    inventory.add_product("sauce-labs-backpack")
    inventory.add_product("sauce-labs-bike-light")
    inventory.verify_cart_count("2")
    
def test_continue_shopping(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.load()
    login.login_with_credentials(Config.USERNAME,Config.PASSWORD)

    inventory.add_product("sauce-labs-backpack")
    inventory.open_cart()
    cart.continue_shopping()

    inventory.verify_inventory_page()            

def test_checkout_information(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.load()
    login.login_with_credentials(Config.USERNAME,Config.PASSWORD)

    inventory.add_product("sauce-labs-backpack")
    inventory.open_cart()
    cart.checkout()

    checkout.fill_information("test", "test", "94335")
    checkout.continue_checkout()

    checkout.verify_overview_page()

def test_complete_order(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.load()
    login.login_with_credentials(Config.USERNAME,Config.PASSWORD)

    inventory.add_product("sauce-labs-backpack")
    inventory.open_cart()
    cart.checkout()

    checkout.fill_information("test", "test", "94335")
    checkout.continue_checkout()
    checkout.finish()

    checkout.verify_order_complete()        