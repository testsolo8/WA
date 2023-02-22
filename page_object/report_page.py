from playwright.sync_api import Page, expect


class ReportPage:
    def __init__(self, page: Page):
        self.page = page
        self.software_on_computers = SoftwareOnComputers(self)

    def navigate_on_report_page(self, menu: str):
        self.page.frame_locator(
            f"//iframe[@src='/report/#/reports?settings.visibility.layout=false']").locator(f"//label[@class='si si-label available-reports__item__label']//span[@class='si si-label__text'][normalize-space()='Software on computers']").get_by_text(f"{menu}").click()
        self.page.frame_locator(
            f"//iframe[@src='/report/#/reports?settings.visibility.layout=false']"
        ).locator(
            f"//label[@class='si si-label filters__menu__header__report cursor-move']//span[@class='si si-label__text'][normalize-space()='{menu}']"
        ).wait_for(
            state="attached"
        )

    def connected_devices_text(self):
        return (
            self.page.frame_locator(
                "//iframe[@src='/report/#/reports?settings.visibility.layout=false']"
            )
            .locator(
                "label[class='si si-label filters__menu__header__report cursor-move'] span[class='si si-label__text']"
            )
            .text_content()
        )

    def computer_devices_text(self):
        return (
            self.page.frame_locator(
                "//iframe[@src='/report/#/reports?settings.visibility.layout=false']"
            )
            .locator(
                "label[class='si si-label filters__menu__header__report cursor-move'] span[class='si si-label__text']"
            )
            .text_content()
        )

class SoftwareOnComputers:
    def __init__(self, report_page: ReportPage):
        self.page = report_page.page
        self.report_page = report_page

    def software_on_computers_text(self):
        return (
            self.page.frame_locator(
                "//iframe[@src='/report/#/reports?settings.visibility.layout=false']"
            )
            .locator(
                "label[class='si si-label filters__menu__header__report cursor-move'] span[class='si si-label__text']"
            )
            .text_content()
        )

    def software_on_computers_create_report_button(self, button_name):
        return self.page.frame_locator("//iframe[@src='/report/#/reports?settings.visibility.layout=false']") \
            .locator(f"//span[normalize-space()='{button_name}']")

