import pytest
from config.settings import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.api_client import APIClient

@pytest.mark.parametrize(
    "username, should_login",
    [
        ("standard_user", True),
        ("problem_user", True),
        ("performance_glitch_user", True),
        ("error_user", True),
        ("visual_user", True),
    ]
)
def test_login_users(page, username, should_login):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()
    login_page.login_with_credentials(username, "secret_sauce")

    if should_login:
        inventory_page.verify_inventory_loaded()
    else:
        login_page.validate_error_message()

def test_login_locked_out_user(page):

    login_page = LoginPage(page)

    login_page.load()
    login_page.login_with_credentials("locked_out_user",Config.PASSWORD)

    login_page.validate_locked_out_error_message()


