import time
from playwright.sync_api import Page

IFRAME = f"iframe >> nth=1"


class ReportPage:
    def __init__(self, page: Page):
        self.page = page
        self.program_controller_reports = ProgramControllerReports(self)
        self.software_on_computers = SoftwareOnComputers(self)
        self.system_reports = SystemReports(self)
        self.iframe = self.page.frame_locator(IFRAME)

    def mask_locator_for_visual_tests(self, cssSelector: str):
        return self.page.locator(cssSelector)

    def navigate_on_report_page(self, menu: str):
        self.iframe.locator(
            f"//label[@class='si si-label available-reports__item__label']//span[@class='si si-label__text'][normalize-space()='{menu}']"
        ).click()
        self.iframe.locator(
            f"//label[@class='si si-label filters__menu__header__report cursor-move']//span[@class='si si-label__text'][normalize-space()='{menu}']"
        ).wait_for(state="attached")

    def left_menu_values(self, name: str):
        return self.iframe.locator(f"(//span[contains(text(),'{name}')])[1]").text_content()

    def connected_devices_text(self):
        return self.iframe.locator(
            "label[class='si si-label filters__menu__header__report cursor-move'] span[class='si si-label__text']"
        ).text_content()

    def computer_devices_text(self):
        return self.iframe.locator(
            "label[class='si si-label filters__menu__header__report cursor-move'] span[class='si si-label__text']"
        ).text_content()

    def create_report_button(self, button_name: str):  # имя кнопки создания отчета
        return self.iframe.locator(f"//span[normalize-space()='{button_name}']")

    def filling_first_placeholder_of_calendar(self, placeholder: str, date: str):  # заполнение первого поля календаря
        self.iframe.locator(
            f"//div[@class='si-date-picker si-date-range-picker__from']//input[@placeholder='{placeholder}']"
        ).fill(date)


class ProgramControllerReports:
    def __init__(self, report_page: ReportPage):
        self.page = report_page.page
        self.report_page = report_page
        self.iframe = self.page.frame_locator(IFRAME)

    def open_calendar_button(self):  # кнопка открытия календаря с фильтре
        return self.iframe.locator(f"(//button[@class='si-btn si-brd si-btn--input si-btn--square'])[1]").click()

    def select_year(self, year: str):  # кнопка выбора года
        return self.iframe.locator(f"//div[normalize-space()='{year}']").click()

    def select_month(self, month: str):  # кнопка выбора месяца
        return self.iframe.locator(f"//div[normalize-space()='{month}']").click()

    def select_full_month(self):  # кнопка выбора полного диапазона месяца
        return self.iframe.locator(
            f"(//div[@class='wa-date-picker__weeks__week wa-date-picker__weeks__week--selected'])[1]"
        ).click()

    def adminisws01_user_data(self, selector: str):  # возвращает данные пользователя adminis@ws01
        return self.iframe.locator(f"{selector}").inner_text().split()

    def bweinmsilocal_user_data(self, selector: str):  # возвращает данные пользователя bwein@msi.local
        return self.iframe.locator(selector).inner_text().split()

    def worktime_log_detail_by_day(self):  # возвращает детальный журнал рабочего времени
        time.sleep(1)
        return self.iframe.locator(f"(//div[@class='work-time-journal__container--cell-2'])[1]").inner_text().split()


class SoftwareOnComputers:
    def __init__(self, report_page: ReportPage):
        self.page = report_page.page
        self.report_page = report_page
        self.iframe = self.page.frame_locator(IFRAME)

    def software_on_computers_text(self):
        return self.iframe.locator(
            "label[class='si si-label filters__menu__header__report cursor-move'] span[class='si si-label__text']"
        ).text_content()

    def all_computers_with_soft(self):
        return self.iframe.locator(f"//div[@class='programs-on-computers-widget__left__block']").inner_text().split()

    def table_selector_with_installed_software(self):
        return self.iframe.locator(f"div[class='wa-simple-table'] table").inner_text().split("\n")

    def computers(self, computer_name: str):
        return self.iframe.locator(
            f"//div[@class='programs-on-computers-widget__left__item']//div[contains(text(),'{computer_name}')]"
        )

    """Блок для данных об измененном софте на компах"""

    def navigate_to_changes_in_software(self, menu_name: str):
        self.iframe.locator("(//label[@class='si si-label si-combobox__input'])[1]").click()
        self.iframe.locator(
            f"//label[@class='si si-label']//span[@class='si si-label__text'][normalize-space()='{menu_name}']"
        ).click()


class SystemReports:
    def __init__(self, report_page: ReportPage):
        self.page = report_page.page
        self.report_page = report_page
        self.iframe = self.page.frame_locator(IFRAME)

    def computers_inactive_active_agent_text(self):
        return self.iframe.locator(
            f"//label[@class='si si-label filters__menu__header__report cursor-move']//span[@class='si si-label__text']"
        ).text_content()
