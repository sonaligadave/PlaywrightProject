from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator('[data-test="title"]')
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')
        self.app_logo = page.get_by_text("Swag Labs")

    def verify_inventory_loaded(self):
        self.wait_for_visible(self.title)

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)

    def verify_logged_out(self):
        self.wait_for_visible(self.app_logo)