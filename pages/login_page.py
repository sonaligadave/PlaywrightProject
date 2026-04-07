from pages.base_page import BasePage
from config.settings import Config

from playwright.sync_api import Playwright, sync_playwright, expect



class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.locked_error = page.locator("[data-test=\"error\"]")

    def load(self):
        self.navigate(Config.BASE_URL)

    def login_with_credentials(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def validate_error_message(self):
         expect(self.locked_error).to_be_visible()
         expect(self.locked_error).to_contain_text("Epic sadface: Username and password do not match any user in this service")

    def validate_locked_out_error_message(self):
         expect(self.locked_error).to_be_visible()
         expect(self.locked_error).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
