# def test_connected_devices_text(main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth):
#     desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
#     desktop_app_auth.report_page.navigate_on_report_page(menu=report_navigate_buttons_software_on_computers.connected_devices)
#     assert desktop_app_auth.report_page.connected_devices_text() == report_navigate_buttons_software_on_computers.connected_devices
#
#
# def test_computer_devices_text(main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth):
#     desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
#     desktop_app_auth.report_page.navigate_on_report_page(menu=report_navigate_buttons_software_on_computers.computer_devices)
#     assert desktop_app_auth.report_page.computer_devices_text() == report_navigate_buttons_software_on_computers.computer_devices


class TestProgramControllerReports:
    def test_program_controller_reports_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.programController_reports
            )
            == report_navigate_buttons_program_controller_reports.programController_reports
        )

    def test_early_departures_from_work_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.early_departures_from_work
            )
            == report_navigate_buttons_program_controller_reports.early_departures_from_work
        )

    def test_late_arrivals_work_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.late_arrivals_work
            )
            == report_navigate_buttons_program_controller_reports.late_arrivals_work
        )

    def test_worktime_log_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.worktime_log
            )
            == report_navigate_buttons_program_controller_reports.worktime_log
        )

    def test_users_efficiency_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.users_efficiency
            )
            == report_navigate_buttons_program_controller_reports.users_efficiency
        )

    def test_timesheet_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(report_navigate_buttons_program_controller_reports.timesheet)
            == report_navigate_buttons_program_controller_reports.timesheet
        )

    def test_total_time_user_work_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.total_time_user_work
            )
            == report_navigate_buttons_program_controller_reports.total_time_user_work
        )

    def test_total_activity_processes_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.total_activity_processes
            )
            == report_navigate_buttons_program_controller_reports.total_activity_processes
        )

    def test_total_activity_websites_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.total_activity_websites
            )
            == report_navigate_buttons_program_controller_reports.total_activity_websites
        )

    def test_total_activity_processes_websites_text(
        self, main_navigate_buttons, report_navigate_buttons_program_controller_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_program_controller_reports.total_activity_processes_websites
            )
            == report_navigate_buttons_program_controller_reports.total_activity_processes_websites
        )

    def test_early_departures_from_work_adminisws01(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.early_departures_from_work
        )
        desktop_app_auth.report_page.program_controller_reports.open_calendar_button()
        desktop_app_auth.report_page.program_controller_reports.select_year(year="2023")
        desktop_app_auth.report_page.program_controller_reports.select_month(month=main_navigate_buttons.january)
        desktop_app_auth.report_page.program_controller_reports.select_full_month()
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.adminisws01_user_data(
            selector=f"(//div[contains(@class,'wa-table-calendar-2__row')])[1]"
        )
        filtered_inner_text = []
        for value in inner_text:
            if "@" in value:
                filtered_inner_text.append(value)
            elif value.endswith(("Days:", "Dias:", "Дней:")) and value[0].isdigit():
                value = value.replace("Days:", "").replace("Dias:", "").replace("Дней:", "")
                filtered_inner_text.append(value)
            elif ":" in value:
                parts = value.split(":")
                if parts[0].isdigit() and parts[1].isdigit():
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {"adminis@ws01", "01:45"}

    def test_early_departures_from_work_bweinmsilocal(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.early_departures_from_work
        )
        desktop_app_auth.report_page.program_controller_reports.open_calendar_button()
        desktop_app_auth.report_page.program_controller_reports.select_year(year="2023")
        desktop_app_auth.report_page.program_controller_reports.select_month(month=main_navigate_buttons.january)
        desktop_app_auth.report_page.program_controller_reports.select_full_month()
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.bweinmsilocal_user_data(
            selector=f"(//div[contains(@class,'wa-table-calendar-2__row')])[2]"
        )
        filtered_inner_text = []
        for value in inner_text:
            if "@" in value:
                filtered_inner_text.append(value)
            elif value.endswith(("Days:", "Dias:", "Дней:")) and value[0].isdigit():
                value = value.replace("Days:", "").replace("Dias:", "").replace("Дней:", "")
                filtered_inner_text.append(value)
            elif ":" in value:
                parts = value.split(":")
                if parts[0].isdigit() and parts[1].isdigit():
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {"bwein@msi.local", "02:01", "04:25", "01:36", "08:03"}

    def test_late_arrivals_work_adminisws01(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.late_arrivals_work
        )
        desktop_app_auth.report_page.program_controller_reports.open_calendar_button()
        desktop_app_auth.report_page.program_controller_reports.select_year(year="2023")
        desktop_app_auth.report_page.program_controller_reports.select_month(month=main_navigate_buttons.january)
        desktop_app_auth.report_page.program_controller_reports.select_full_month()
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.adminisws01_user_data(
            selector=f"(//div[contains(@class,'wa-table-calendar-2__row')])[1]"
        )
        filtered_inner_text = []
        for value in inner_text:
            if "@" in value:
                filtered_inner_text.append(value)
            elif value.endswith(("Days:", "Dias:", "Дней:")) and value[0].isdigit():
                value = value.replace("Days:", "").replace("Dias:", "").replace("Дней:", "")
                filtered_inner_text.append(value)
            elif ":" in value:
                parts = value.split(":")
                if parts[0].isdigit() and parts[1].isdigit():
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {"adminis@ws01", "05:58"}

    def test_late_arrivals_work_bweinmsilocal(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.late_arrivals_work
        )
        desktop_app_auth.report_page.program_controller_reports.open_calendar_button()
        desktop_app_auth.report_page.program_controller_reports.select_year(year="2023")
        desktop_app_auth.report_page.program_controller_reports.select_month(month=main_navigate_buttons.january)
        desktop_app_auth.report_page.program_controller_reports.select_full_month()
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.bweinmsilocal_user_data(
            selector=f"(//div[contains(@class,'wa-table-calendar-2__row')])[2]"
        )
        filtered_inner_text = []
        for value in inner_text:
            if "@" in value:
                filtered_inner_text.append(value)
            elif value.endswith(("Days:", "Dias:", "Дней:")) and value[0].isdigit():
                value = value.replace("Days:", "").replace("Dias:", "").replace("Дней:", "")
                filtered_inner_text.append(value)
            elif ":" in value:
                parts = value.split(":")
                if parts[0].isdigit() and parts[1].isdigit():
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {"bwein@msi.local", "03:18", "08:56", "05:37"}

    def test_worktime_log_adminisws01(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.worktime_log
        )
        desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
            placeholder=main_navigate_buttons.first_date_range_placeholder, date="03.01.2023"
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.adminisws01_user_data(
            selector=f"(//div[contains(@class,'wa-table__row wa-table--selected')])[1]"
        )
        assert ",".join(inner_text).replace(",", "") == "adminis@ws0114:58:1416:14:3401:16:1901:16:1900:49:2200:49:22"

    def test_worktime_log_bweinmsilocal(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.worktime_log
        )
        desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
            placeholder=main_navigate_buttons.first_date_range_placeholder, date="03.01.2023"
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.bweinmsilocal_user_data(
            selector=f"(//div[@class='wa-table__row'])[2]"
        )
        assert (
            ",".join(inner_text).replace(",", "") == "bwein@msi.local07:48:3017:10:0609:21:3584:14:1802:56:0926:25:21"
        )

    def test_worktime_log_adminisws01_detail_by_day(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.worktime_log
        )
        desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
            placeholder=main_navigate_buttons.first_date_range_placeholder, date="03.01.2023"
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.worktime_log_detail_by_day()
        filtered_inner_text = []
        for value in inner_text:
            if ":" in value or "." in value:
                parts = value.split(":") if ":" in value else value.split(".")
                if all(part.isdigit() for part in parts):
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {"27.01.2023", "14:58:14", "16:14:34", "01:16:19", "00:49:22"}

    def test_worktime_log_bweinmsilocal_detail_by_day(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.worktime_log
        )
        desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
            placeholder=main_navigate_buttons.first_date_range_placeholder, date="03.01.2023"
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        desktop_app_auth.report_page.page.frame_locator("iframe >> nth=1").locator(
            "(//span[contains(text(),'bwein@msi.local')])[1]"
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.worktime_log_detail_by_day()
        filtered_inner_text = []
        for value in inner_text:
            if ":" in value or "." in value:
                parts = value.split(":") if ":" in value else value.split(".")
                if all(part.isdigit() for part in parts):
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {
            "25.01.2023",
            "12:18:17",
            "15:58:21",
            "03:40:04",
            "01:22:44",
            "26.01.2023",
            "08:23:19",
            "13:34:42",
            "05:11:23",
            "00:44:49",
            "27.01.2023",
            "14:37:45",
            "16:23:10",
            "01:45:24",
            "00:14:04",
            "30.01.2023",
            "00:31:56",
            "23:59:59",
            "23:28:03",
            "02:31:13",
            "31.01.2023",
            "00:00:00",
            "18:54:02",
            "18:54:02",
            "04:26:23",
            "01.02.2023",
            "08:44:45",
            "18:24:59",
            "09:40:14",
            "05:19:46",
            "02.02.2023",
            "08:19:23",
            "18:17:03",
            "09:57:39",
            "07:17:58",
            "03.02.2023",
            "08:36:58",
            "17:04:44",
            "08:27:45",
            "03:15:14",
            "06.02.2023",
            "08:44:12",
            "11:53:56",
            "03:09:44",
            "01:13:10",
        }

    def test_timesheet_adminisws01(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.timesheet
        )
        desktop_app_auth.report_page.program_controller_reports.open_calendar_button()
        desktop_app_auth.report_page.program_controller_reports.select_year(year="2023")
        desktop_app_auth.report_page.program_controller_reports.select_month(month=main_navigate_buttons.january)
        desktop_app_auth.report_page.program_controller_reports.select_full_month()
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.adminisws01_user_data(
            selector=f"(//div[@class='wa-table-calendar-2__row'])[1]"
        )
        filtered_inner_text = []
        for value in inner_text:
            if "@" in value:
                filtered_inner_text.append(value)
            elif value.endswith(("Days:", "Dias:", "Дней:", "Días:")) and value[0].isdigit():
                value = value.replace("Days:", "").replace("Dias:", "").replace("Дней:", "").replace("Días:", "")
                if ":" in value:
                    parts = value[:5]
                    parts2 = value[5:]
                    filtered_inner_text.extend([parts, parts2])
            elif ":" in value:
                parts = value.split(":")
                if parts[0].isdigit() and parts[1].isdigit():
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {"adminis@ws01", "14:58", "16:14", "01:16", "00:49"}

    def test_timesheet_bweinmsilocal(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_program_controller_reports.timesheet
        )
        desktop_app_auth.report_page.program_controller_reports.open_calendar_button()
        desktop_app_auth.report_page.program_controller_reports.select_year(year="2023")
        desktop_app_auth.report_page.program_controller_reports.select_month(month=main_navigate_buttons.january)
        desktop_app_auth.report_page.program_controller_reports.select_full_month()
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        inner_text = desktop_app_auth.report_page.program_controller_reports.adminisws01_user_data(
            selector=f"(//div[@class='wa-table-calendar-2__row'])[2]"
        )
        filtered_inner_text = []
        for value in inner_text:
            if "@" in value:
                filtered_inner_text.append(value)
            elif value.endswith(("Days:", "Dias:", "Дней:", "Días:")) and value[0].isdigit():
                value = value.replace("Days:", "").replace("Dias:", "").replace("Дней:", "").replace("Días:", "")
                if ":" in value:
                    parts = value[:5]
                    parts2 = value[5:]
                    filtered_inner_text.extend([parts, parts2])
            elif value.endswith(("Act-ty:", "Act-ad:", "Акт-ть:")) and value[0].isdigit():
                value = value.replace("Act-ty:", "").replace("Act-ad:", "").replace("Акт-ть:", "")
                filtered_inner_text.append(value)
            elif ":" in value:
                parts = value.split(":")
                if len(parts[1]) == 4 and parts[1].isdigit():
                    a = value[:5]
                    b = value[5:]
                    filtered_inner_text.extend([a, b])
                elif parts[0].isdigit() and parts[1].isdigit():
                    filtered_inner_text.append(value)
        assert set(filtered_inner_text) == {
            "bwein@msi.local",
            "12:18",
            "15:58",
            "03:40",
            "01:22",
            "08:23",
            "13:34",
            "05:11",
            "00:44",
            "14:37",
            "16:23",
            "01:45",
            "00:14",
            "52:58",
            "09:19",
        }


class TestSoftwareOnComputers:
    def test_software_reports_text(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(
                report_navigate_buttons_software_on_computers.software_reports
            )
            == report_navigate_buttons_software_on_computers.software_reports
        )

    def test_software_on_computers_text(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        assert (
            desktop_app_auth.report_page.software_on_computers.software_on_computers_text()
            == report_navigate_buttons_software_on_computers.software_on_computers
        )

    def test_all_computers_with_soft(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        objects_locator = desktop_app_auth.report_page.software_on_computers.all_computers_with_soft()
        assert set(zip(objects_locator[::2], objects_locator[1::2])) == {
            ("AC1.msi.local", "120"),
            ("RCOK.msi.local", "14"),
            ("W10.msi.local", "33"),
            ("ws01", "167"),
            ("WS01.msi.local", "178"),
            ("WS10.msi.local", "16"),
            ("WS11.msi.local", "56"),
        }

    def test_soft_on_computer_RCOK_msi_local(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        desktop_app_auth.report_page.software_on_computers.computers(computer_name="RCOK.msi.local").click()
        objects_locator = desktop_app_auth.report_page.software_on_computers.table_selector_with_installed_software()
        objects_locator_without_digit = {
            string
            for string in objects_locator
            if not (string.isdigit() or string.replace(".", "").isdigit())
            and string.strip() != ""
            and "\t" not in string
        }
        assert objects_locator_without_digit == {
            "Microsoft Visual C++ 2008 Redistributable - x86",
            "Google Update Helper",
            "SearchInform Client",
            "Search Corporate API",
            "SearchInform ReportCenter",
            "VMware Tools",
            "Microsoft SQL Server 2008 R2 Native Client",
            "SearchInform DataCenter",
            "Far Manager 3 x64",
            "Microsoft Visual C++ 2008 Redistributable - x64",
            "Microsoft Windows Server 2008 R2 Standard x64 Service Pack 1",
            "Google Chrome",
            "TeamViewer 10",
            "Search API",
        }

    def test_soft_on_computer_W10_msi_local(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        desktop_app_auth.report_page.software_on_computers.computers(computer_name="W10.msi.local").click()
        objects_locator = desktop_app_auth.report_page.software_on_computers.table_selector_with_installed_software()
        objects_locator_without_digit = {
            string
            for string in objects_locator
            if not (string.isdigit() or string.replace(".", "").isdigit())
            and string.strip() != ""
            and "\t" not in string
        }
        assert objects_locator_without_digit == {
            "Postman x86_64",
            "Search API",
            "Mozilla Firefox",
            "Python Core Interpreter",
            "Python Standard Library",
            "DBeaver",
            "Mozilla Maintenance Service",
            "SearchInform DataCenter",
            "VMware Tools",
            "Microsoft Visual C++ 2008 Redistributable - x86",
            "Microsoft Edge WebView2 Runtime",
            "Python Executables",
            "Python Documentation",
            "EndpointController",
            "Microsoft Windows 10 Enterprise N x64",
            "Python Launcher",
            "Python Tcl/Tk Support",
            "Microsoft Visual C++ 2008 Redistributable - x64",
            "Python Test Suite",
            "psqlODBC_x64",
            "Python pip Bootstrap",
            "Python Utility Scripts",
            "Search Server 64",
            "Librasoft AnalyticConsole",
            "Microsoft SQL Server 2012 Native Client",
            "Far Manager 3",
            "Google Update Helper",
            "Google Chrome",
            "Microsoft OneDrive",
            "PyCharm Community Edition",
            "Python Development Libraries",
            "psqlODBC",
            "Python",
        }

    def test_soft_on_computer_WS10_msi_local(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        desktop_app_auth.report_page.software_on_computers.computers(computer_name="WS10.msi.local").click()
        objects_locator = desktop_app_auth.report_page.software_on_computers.table_selector_with_installed_software()
        objects_locator_without_digit = {
            string
            for string in objects_locator
            if not (string.isdigit() or string.replace(".", "").isdigit())
            and string.strip() != ""
            and "\t" not in string
        }
        assert objects_locator_without_digit == {
            "Microsoft Visual C++ 2008 Redistributable - x86",
            "VMware Tools",
            "Google Update Helper",
            "Far Manager 3",
            "SearchInform DataCenter API",
            "Search API",
            "Microsoft OneDrive",
            "Search Corporate API",
            "SearchInform AnalyticConsole",
            "SearchInform EndpointController",
            "Майкрософт Windows 10 Pro x86",
            "Skype",
            "SearchInform DataCenter",
            "Microsoft SQL Server 2012 Native Client",
            "Microsoft SQL Server 2008 R2 Native Client",
            "Google Chrome",
        }

    class TestReportPageChangedSoftwareOnComputers:
        def test_all_computers_with_changed_soft(
            self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
        ):
            desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
            desktop_app_auth.report_page.navigate_on_report_page(
                menu=report_navigate_buttons_software_on_computers.software_on_computers
            )
            desktop_app_auth.report_page.software_on_computers.navigate_to_changes_in_software(
                menu_name=report_navigate_buttons_software_on_computers.dropdown_list_show
            )
            desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
                placeholder=report_navigate_buttons_software_on_computers.first_date_range_placeholder,
                date="24.02.2022",
            )
            desktop_app_auth.report_page.create_report_button(
                button_name=main_navigate_buttons.create_report_buttons
            ).click()
            objects_locator = desktop_app_auth.report_page.software_on_computers.all_computers_with_soft()
            assert set(zip(objects_locator[::2], objects_locator[1::2])) == {
                ("AC1.msi.local", "134"),
                ("W10.msi.local", "34"),
                ("WS01.msi.local", "15"),
                ("WS10.msi.local", "17"),
                ("WS11.msi.local", "59"),
                ("ws01", "182"),
            }

        def test_changed_soft_on_computer_W10_msi_local(
            self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
        ):
            desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
            desktop_app_auth.report_page.navigate_on_report_page(
                menu=report_navigate_buttons_software_on_computers.software_on_computers
            )
            desktop_app_auth.report_page.software_on_computers.navigate_to_changes_in_software(
                menu_name=report_navigate_buttons_software_on_computers.dropdown_list_show
            )
            desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
                placeholder=report_navigate_buttons_software_on_computers.first_date_range_placeholder,
                date="24.02.2022",
            )
            desktop_app_auth.report_page.create_report_button(
                button_name=main_navigate_buttons.create_report_buttons
            ).click()
            desktop_app_auth.report_page.software_on_computers.computers(computer_name="W10.msi.local").click()
            objects_locator = (
                desktop_app_auth.report_page.software_on_computers.table_selector_with_installed_software()
            )
            objects_locator_without_digit = {
                string
                for string in objects_locator
                if not (string.isdigit() or string.replace(".", "").isdigit())
                and string.strip() != ""
                and "\t" not in string
            }
            assert objects_locator_without_digit == {
                "Python Documentation",
                "Python Test Suite",
                "Python Utility Scripts",
                "Mozilla Maintenance Service",
                "DBeaver",
                "Microsoft Visual C++ 2008 Redistributable - x86",
                "Microsoft Edge WebView2 Runtime",
                "Python",
                "Search API",
                "Postman x86_64",
                "Python Launcher",
                "Python Tcl/Tk Support",
                "Far Manager 3",
                "Python pip Bootstrap",
                "Microsoft Visual C++ 2008 Redistributable - x64",
                "SearchInform DataCenter",
                "Python Executables",
                "Search Server 64",
                "VMware Tools",
                "psqlODBC",
                "Google Chrome",
                "Python Development Libraries",
                "EndpointController",
                "Librasoft AnalyticConsole",
                "Google Update Helper",
                "Python Standard Library",
                "Microsoft SQL Server 2012 Native Client",
                "Mozilla Firefox",
                "PyCharm Community Edition",
                "Python Core Interpreter",
                "Microsoft OneDrive",
                "Microsoft Windows 10 Enterprise N x64",
                "psqlODBC_x64",
            }

        def test_changed_soft_on_computer_WS01_msi_local(
            self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
        ):
            desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
            desktop_app_auth.report_page.navigate_on_report_page(
                menu=report_navigate_buttons_software_on_computers.software_on_computers
            )
            desktop_app_auth.report_page.software_on_computers.navigate_to_changes_in_software(
                menu_name=report_navigate_buttons_software_on_computers.dropdown_list_show
            )
            desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
                placeholder=report_navigate_buttons_software_on_computers.first_date_range_placeholder,
                date="24.02.2022",
            )
            desktop_app_auth.report_page.create_report_button(
                button_name=main_navigate_buttons.create_report_buttons
            ).click()
            desktop_app_auth.report_page.software_on_computers.computers(computer_name="WS01.msi.local").click()
            objects_locator = (
                desktop_app_auth.report_page.software_on_computers.table_selector_with_installed_software()
            )
            objects_locator_without_digit = {
                string
                for string in objects_locator
                if not (string.isdigit() or string.replace(".", "").isdigit())
                and string.strip() != ""
                and "\t" not in string
            }
            assert objects_locator_without_digit == {
                "Mozilla Firefox",
                "Update for Microsoft Office 2013 32-Bit Edition",
                "psqlODBC_x64",
                "Update for Microsoft Project 2013 32-Bit Edition",
                "Update for Microsoft Publisher 2013 32-Bit Edition",
                "Security Update for Microsoft Project 2013 32-Bit Edition",
                "Security Update for Microsoft Access 2013 32-Bit Edition",
                "Security Update for Microsoft Publisher 2013 32-Bit Edition",
                "Update for Microsoft Outlook 2013 32-Bit Edition",
                "Postman x86_64",
                "psqlODBC",
                "Security Update for Microsoft Office 2013 32-Bit Edition",
                "Security Update for Microsoft Outlook 2013 32-Bit Edition",
                "Update for Microsoft Access 2013 32-Bit Edition",
                "Update for Microsoft .NET Framework",
            }

        def test_changed_soft_on_computer_WS10_msi_local(
            self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
        ):
            desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
            desktop_app_auth.report_page.navigate_on_report_page(
                menu=report_navigate_buttons_software_on_computers.software_on_computers
            )
            desktop_app_auth.report_page.software_on_computers.navigate_to_changes_in_software(
                menu_name=report_navigate_buttons_software_on_computers.dropdown_list_show
            )
            desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
                placeholder=report_navigate_buttons_software_on_computers.first_date_range_placeholder,
                date="24.02.2022",
            )
            desktop_app_auth.report_page.create_report_button(
                button_name=main_navigate_buttons.create_report_buttons
            ).click()
            desktop_app_auth.report_page.software_on_computers.computers(computer_name="WS10.msi.local").click()
            objects_locator = (
                desktop_app_auth.report_page.software_on_computers.table_selector_with_installed_software()
            )
            objects_locator_without_digit = {
                string
                for string in objects_locator
                if not (string.isdigit() or string.replace(".", "").isdigit())
                and string.strip() != ""
                and "\t" not in string
            }
            assert objects_locator_without_digit == {
                "Skype",
                "Microsoft Visual C++ 2008 Redistributable - x86",
                "Майкрософт Windows 10 Pro x86",
                "Search Corporate API",
                "SearchInform DataCenter",
                "Microsoft SQL Server 2012 Native Client",
                "Google Update Helper",
                "Microsoft OneDrive",
                "SearchInform AnalyticConsole",
                "SearchInform DataCenter API",
                "SearchInform EndpointController",
                "VMware Tools",
                "Microsoft SQL Server 2008 R2 Native Client",
                "Google Chrome",
                "Search API",
                "Far Manager 3",
            }

        def test_difference_of_changes_WS01_msi_local(
            self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth
        ):
            desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
            desktop_app_auth.report_page.navigate_on_report_page(
                menu=report_navigate_buttons_software_on_computers.software_on_computers
            )
            desktop_app_auth.report_page.software_on_computers.navigate_to_changes_in_software(
                menu_name=report_navigate_buttons_software_on_computers.dropdown_list_show
            )
            desktop_app_auth.report_page.filling_first_placeholder_of_calendar(
                placeholder=report_navigate_buttons_software_on_computers.first_date_range_placeholder,
                date="24.02.2022",
            )
            desktop_app_auth.report_page.create_report_button(
                button_name=main_navigate_buttons.create_report_buttons
            ).click()
            desktop_app_auth.report_page.software_on_computers.computers(computer_name="WS01.msi.local").click()
            xlink_href_values = []
            for iframe_element in desktop_app_auth.report_page.page.query_selector_all("iframe"):
                # Получение контекста страницы внутри iframe
                frame = iframe_element.content_frame()
                if not frame:
                    continue
                # Получение всех значений атрибута xlink:href внутри use внутри iframe
                for element in frame.query_selector_all("use[*|href^='#devices-changes-computers']"):
                    xlink_href_value = element.evaluate("node => node.getAttribute('xlink:href')")
                    xlink_href_values.append(xlink_href_value)
            removed_list = [item for item in xlink_href_values if item == "#devices-changes-computers__removed"]
            added_list = [item for item in xlink_href_values if item == "#devices-changes-computers__added"]
            assert len(removed_list) == 6
            assert len(added_list) == 9


class TestSystemReports:
    def test_system_reports_text(self, main_navigate_buttons, report_navigate_buttons_system_reports, desktop_app_auth):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        assert (
            desktop_app_auth.report_page.left_menu_values(report_navigate_buttons_system_reports.system_reports)
            == report_navigate_buttons_system_reports.system_reports
        )

    def test_computers_inactive_active_agent_text(
        self, main_navigate_buttons, report_navigate_buttons_system_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_system_reports.computers_inactive_active_agent
        )
        assert (
            desktop_app_auth.report_page.system_reports.computers_inactive_active_agent_text()
            == report_navigate_buttons_system_reports.computers_inactive_active_agent
        )

    def test_computers_without_agents_text(
        self, main_navigate_buttons, report_navigate_buttons_system_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_system_reports.computers_without_agents
        )
        assert (
            desktop_app_auth.report_page.system_reports.computers_inactive_active_agent_text()
            == report_navigate_buttons_system_reports.computers_without_agents
        )

    def test_number_of_messages_computers_text(
        self, main_navigate_buttons, report_navigate_buttons_system_reports, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_system_reports.number_of_messages_computers
        )
        assert (
            desktop_app_auth.report_page.system_reports.computers_inactive_active_agent_text()
            == report_navigate_buttons_system_reports.number_of_messages_computers
        )
