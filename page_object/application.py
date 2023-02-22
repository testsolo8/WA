import logging
from playwright.sync_api import Browser, ConsoleMessage, Dialog
from page_object.login_page import LoginPage
from page_object.report_page import ReportPage


class App:
    def __init__(
        self,
        browser: Browser,
        base_url: str,
        ignore_https_errors: bool = None,
        **kwargs,
    ):
        self.browser = browser
        self.ignore_https_errors = ignore_https_errors
        self.context = self.browser.new_context(
            ignore_https_errors=ignore_https_errors, **kwargs
        )
        self.page = self.context.new_page()
        self.base_url = base_url
        self.login_page = LoginPage(self.page)
        self.report_page = ReportPage(self.page)

        def console_handler(message: ConsoleMessage):
            if message.type == "error":
                logging.error(f"page: {self.page.url}, console error: {message.text}")

        def dialog_handler(dialog: Dialog):
            logging.warning(f"page: {self.page.url}, dialog text: {dialog.message}")
            dialog.accept()

        self.page.on("console", console_handler)
        self.page.on("dialog", dialog_handler)

    def trace(self):
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    def trace_stop(self):
        self.context.tracing.stop(path="trace.zip")

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def navigate_to(self, menu: str):
        self.page.click(f"//button[@title='{menu}']")
        self.page.wait_for_load_state()

    def login(self, login: str, password: str):
        self.page.locator("[name ='username']").fill(f"{login}")
        self.page.locator("[name ='password']").fill(f"{password}")
        self.page.locator("//button[@class='si si-button']").click()

    def choice_language(self, lang: str):
        self.page.click(
            f"label[class='si si-label si-combobox__input'] span[class='si si-label__text']"
        )
        self.page.click(f"text={lang}")

    def close(self):
        self.page.close()
        self.context.close()
