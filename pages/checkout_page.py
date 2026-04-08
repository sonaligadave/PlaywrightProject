from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def fill_information(self, first, last, postal):
        self.page.locator('[data-test="firstName"]').fill(first)
        self.page.locator('[data-test="lastName"]').fill(last)
        self.page.locator('[data-test="postalCode"]').fill(postal)

    def continue_checkout(self):
        self.page.locator('[data-test="continue"]').click()

    def verify_overview_page(self):
        assert self.page.locator('[data-test="total-info-label"]').is_visible()
        assert self.page.locator('[data-test="payment-info-label"]').is_visible()
        assert self.page.locator('[data-test="shipping-info-label"]').is_visible()

    def finish(self):
        self.page.locator('[data-test="finish"]').click()

    def verify_order_complete(self):
        assert self.page.locator('[data-test="pony-express"]').is_visible()
        assert self.page.locator('[data-test="complete-text"]').is_visible()
        assert self.page.locator('[data-test="back-to-products"]').is_visible()