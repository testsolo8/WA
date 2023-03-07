import time

THRESHOLD = 0.1
APP_VERSION = "label[class='si si-label si-app__version'] span[class='si si-label__text']"


class TestProgramControllerReportsVisual:
    def test_early_departures_from_work_adminisws01_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_early_departures_from_work_bweinmsilocal_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_late_arrivals_work_adminisws01_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_late_arrivals_work_bweinmsilocal_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_worktime_log_adminisws01_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_worktime_log_bweinmsilocal_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_worktime_log_adminisws01_detail_by_day_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_worktime_log_bweinmsilocal_detail_by_day_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_timesheet_adminisws01_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_timesheet_bweinmsilocal_visual(
        self,
        main_navigate_buttons,
        report_navigate_buttons_program_controller_reports,
        desktop_app_auth,
        assert_snapshot,
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
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )


class TestSoftwareOnComputers:
    def test_all_computers_with_soft_visual(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth, assert_snapshot
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_soft_on_computer_RCOK_msi_local_visual(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth, assert_snapshot
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        desktop_app_auth.report_page.software_on_computers.computers(computer_name="RCOK.msi.local").click()
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_soft_on_computer_W10_msi_local_visual(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth, assert_snapshot
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        desktop_app_auth.report_page.software_on_computers.computers(computer_name="W10.msi.local").click()
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    def test_soft_on_computer_WS10_msi_local_visual(
        self, main_navigate_buttons, report_navigate_buttons_software_on_computers, desktop_app_auth, assert_snapshot
    ):
        desktop_app_auth.navigate_to(menu=main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(
            menu=report_navigate_buttons_software_on_computers.software_on_computers
        )
        desktop_app_auth.report_page.create_report_button(
            button_name=main_navigate_buttons.create_report_buttons
        ).click()
        desktop_app_auth.report_page.software_on_computers.computers(computer_name="WS10.msi.local").click()
        time.sleep(2)
        assert_snapshot(
            desktop_app_auth.page.screenshot(
                full_page=True,
                mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
            ),
            threshold=THRESHOLD,
        )

    class TestReportPageChangedSoftwareOnComputers:
        def test_all_computers_with_changed_soft_visual(
            self,
            main_navigate_buttons,
            report_navigate_buttons_software_on_computers,
            desktop_app_auth,
            assert_snapshot,
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
            time.sleep(2)
            assert_snapshot(
                desktop_app_auth.page.screenshot(
                    full_page=True,
                    mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
                ),
                threshold=THRESHOLD,
            )

        def test_changed_soft_on_computer_W10_msi_local_visual(
            self,
            main_navigate_buttons,
            report_navigate_buttons_software_on_computers,
            desktop_app_auth,
            assert_snapshot,
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
            time.sleep(5)
            assert_snapshot(
                desktop_app_auth.page.screenshot(
                    full_page=True,
                    mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
                ),
                threshold=THRESHOLD,
            )

        def test_changed_soft_on_computer_WS01_msi_local_visual(
            self,
            main_navigate_buttons,
            report_navigate_buttons_software_on_computers,
            desktop_app_auth,
            assert_snapshot,
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
            time.sleep(2)
            assert_snapshot(
                desktop_app_auth.page.screenshot(
                    full_page=True,
                    mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
                ),
                threshold=THRESHOLD,
            )

        def test_changed_soft_on_computer_WS10_msi_local_visual(
            self,
            main_navigate_buttons,
            report_navigate_buttons_software_on_computers,
            desktop_app_auth,
            assert_snapshot,
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
            time.sleep(2)
            assert_snapshot(
                desktop_app_auth.page.screenshot(
                    full_page=True,
                    mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
                ),
                threshold=THRESHOLD,
            )

        def test_difference_of_changes_WS01_msi_local_visual(
            self,
            main_navigate_buttons,
            report_navigate_buttons_software_on_computers,
            desktop_app_auth,
            assert_snapshot,
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
            time.sleep(5)
            assert_snapshot(
                desktop_app_auth.page.screenshot(
                    full_page=True,
                    mask=[desktop_app_auth.report_page.mask_locator_for_visual_tests(cssSelector=APP_VERSION)],
                ),
                threshold=THRESHOLD,
            )
