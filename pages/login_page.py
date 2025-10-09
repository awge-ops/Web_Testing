from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com/"):
        self.page = page
        self.base_url = base_url
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator("h3[data-test='error']")

    def open(self):
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def wait_for_inventory(self, timeout: int = 5000):
        self.page.wait_for_url("**/inventory.html", timeout=timeout)

    def get_error(self) -> str:
        if self.error.count():
            text = self.error.text_content()
            return text.strip() if text else ""
        return ""
