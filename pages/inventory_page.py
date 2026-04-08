from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator('[data-test="title"]')
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')
        self.app_logo = page.get_by_text("Swag Labs")

    def add_product(self, product_id):
        self.page.locator(f'[data-test="add-to-cart-{product_id}"]').click()

    def remove_product(self, product_id):
        self.page.locator(f'[data-test="remove-{product_id}"]').click()

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def verify_inventory_loaded(self):
        self.wait_for_visible(self.title)

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)

    def verify_logged_out(self):
        self.wait_for_visible(self.app_logo)


    def verify_product_added(self, product_id):
        assert self.page.locator(f'[data-test="remove-{product_id}"]').is_visible()

    def verify_product_removed(self, product_id):
        assert self.page.locator(f'[data-test="add-to-cart-{product_id}"]').is_visible()

    def verify_cart_count(self, count):
        assert self.page.locator(".shopping_cart_badge").text_content() == count

    def verify_inventory_page(self):
        assert self.page.locator('[data-test="title"]').is_visible()    