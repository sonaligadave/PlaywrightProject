from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_logout(page):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()
    login_page.login()

    inventory_page.verify_inventory_loaded()
    inventory_page.logout()