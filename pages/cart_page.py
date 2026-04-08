from pages.base_page import BasePage


class CartPage(BasePage):

    def verify_product_present(self, product_name):
        assert self.page.locator(".cart_item").filter(
            has_text=product_name
        ).is_visible()

    def remove_product(self, product_id):
        self.page.locator(f'[data-test="remove-{product_id}"]').click()

    def continue_shopping(self):
        self.page.locator('[data-test="continue-shopping"]').click()

    def checkout(self):
        self.page.locator('[data-test="checkout"]').click()