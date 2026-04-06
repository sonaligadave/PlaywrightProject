from pages.base_page import BasePage
from config.settings import Config


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def load(self):
        self.navigate(Config.BASE_URL)

    def login(self):
        self.fill(self.username_input, Config.USERNAME)
        self.fill(self.password_input, Config.PASSWORD)
        self.click(self.login_button)