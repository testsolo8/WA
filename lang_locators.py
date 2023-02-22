class Language:
    eng = "eng"
    rus = "rus"
    esp = "esp"


class MainNavigateButtons:
    def __init__(self, lang: Language):
        self.language = lang
        self.main_buttons = {
            "report": {
                Language.eng: "Reports",
                Language.rus: "Отчеты",
                Language.esp: "Reportes",
            }
        }
        self.lang_selector = {
            Language.eng: "English",
            Language.rus: "Русский",
            Language.esp: "Español",
        }

    @property
    def report(self):
        return self.main_buttons["report"][self.language]

    @property
    def lang(self):
        return self.lang_selector[self.language]


class ReportNavigationButtons(MainNavigateButtons):
    report_buttons = {
        "connected_devices": {
            Language.eng: "Connected Devices",
            Language.rus: "Подключаемые устройства",
            Language.esp: "Dispositivos conectados",
        },
        "computer_devices": {
            Language.eng: "Computer devices",
            Language.rus: "Устройства на компьютерах",
            Language.esp: "Dispositivos instalados",
        },
        "software_on_computers": {
            Language.eng: "Software on computers",
            Language.rus: "Программы на компьютерах",
            Language.esp: "Software en computadoras",
                "create_report_buttons": {
                    Language.eng: "Create report",
                    Language.rus: "Создать отчет",
                    Language.esp: "Crear reporte",
                }
        },
    }

    @property
    def connected_devices(self):
        return self.report_buttons["connected_devices"][self.language]

    @property
    def computer_devices(self):
        return self.report_buttons["computer_devices"][self.language]

    @property
    def software_on_computers(self):
        return self.report_buttons["software_on_computers"][self.language]

    @property
    def software_on_computers_create_report_buttons(self):
        return self.report_buttons["software_on_computers"]["create_report_buttons"][self.language]
