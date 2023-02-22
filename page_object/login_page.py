from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def check_login_page_exists(self):
        content = self.page.text_content(f"//span[contains(text(),'WebAnalytic')]")
        return content

    def check_login_page_auth_ok(self):
        content = self.page.text_content(
            f"//label[@align='center']//span[@class='si si-label__text'][normalize-space()='Search']"
        )
        return content
