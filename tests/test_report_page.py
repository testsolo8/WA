def test_open_connected_devices(
    main_navigate_buttons, report_navigate_buttons, desktop_app_auth
):
    desktop_app_auth.navigate_to(main_navigate_buttons.report)
    desktop_app_auth.report_page.navigate_on_report_page(
        report_navigate_buttons.connected_devices
    )
    assert (
        desktop_app_auth.report_page.connected_devices_text()
        == report_navigate_buttons.connected_devices
    )


def test_open_computer_devices(
    main_navigate_buttons, report_navigate_buttons, desktop_app_auth
):
    desktop_app_auth.navigate_to(main_navigate_buttons.report)
    desktop_app_auth.report_page.navigate_on_report_page(
        report_navigate_buttons.computer_devices
    )
    assert (
        desktop_app_auth.report_page.computer_devices_text()
        == report_navigate_buttons.computer_devices
    )


class TestReportPageOpenSoftwareOnComputers:
    def test_open_software_on_computers(self,
        main_navigate_buttons, report_navigate_buttons, desktop_app_auth
    ):
        desktop_app_auth.navigate_to(main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(report_navigate_buttons.software_on_computers)
        assert (
            desktop_app_auth.report_page.software_on_computers.software_on_computers_text()
            == report_navigate_buttons.software_on_computers
        )

    def test_report_software_on_computers(self, main_navigate_buttons, report_navigate_buttons, desktop_app_auth):
        desktop_app_auth.navigate_to(main_navigate_buttons.report)
        desktop_app_auth.report_page.navigate_on_report_page(report_navigate_buttons.software_on_computers)
        desktop_app_auth.report_page.software_on_computers.software_on_computers_create_report_button(report_navigate_buttons.software_on_computers_create_report_buttons).click()
