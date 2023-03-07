class Language:
    eng = "eng"
    rus = "rus"
    esp = "esp"


class MainNavigateButtons:  # Описание главных пунктов меню консоли WA
    def __init__(self, lang: Language):
        self.language = lang
        self.main_buttons = {
            "report": {
                Language.eng: "Reports",
                Language.rus: "Отчеты",
                Language.esp: "Reportes",
            },
            "create_report_buttons": {
                Language.eng: "Create report",
                Language.rus: "Создать отчет",
                Language.esp: "Crear reporte",
            },
        }
        self.lang_selector = {
            Language.eng: "English",
            Language.rus: "Русский",
            Language.esp: "Español",
        }
        self.month_name = {
            "January": {Language.eng: "Jan", Language.rus: "Янв", Language.esp: "ene"},
            "February": {Language.eng: "Feb", Language.rus: "Фев", Language.esp: "feb"},
            "March": {Language.eng: "Mar", Language.rus: "Мар", Language.esp: "mar"},
            "April": {Language.eng: "Apr", Language.rus: "Апр", Language.esp: "abr"},
            "May": {Language.eng: "May", Language.rus: "Май", Language.esp: "may"},
            "June": {Language.eng: "Jun", Language.rus: "Июн", Language.esp: "jun"},
            "July": {Language.eng: "Jul", Language.rus: "Июл", Language.esp: "jul"},
            "August": {Language.eng: "Aug", Language.rus: "Авг", Language.esp: "ago"},
            "September": {Language.eng: "Sep", Language.rus: "Сен", Language.esp: "sep"},
            "October": {Language.eng: "Oct", Language.rus: "Окт", Language.esp: "oct"},
            "November": {Language.eng: "Nov", Language.rus: "Ноя", Language.esp: "nov"},
            "December": {Language.eng: "Dec", Language.rus: "Дек", Language.esp: "dic"},
        }
        self.date_range_placeholder = {
            Language.eng: "dd.mm.yyyy",
            Language.rus: "дд.мм.гггг",
            Language.esp: "dd.mm.aaaa",
        }

    @property
    def report(self):
        return self.main_buttons["report"][self.language]

    @property
    def create_report_buttons(self):
        return self.main_buttons["create_report_buttons"][self.language]

    @property
    def lang(self):
        return self.lang_selector[self.language]

    @property
    def january(self):  # возвращает месяц календаря
        return self.month_name["January"][self.language]

    @property
    def first_date_range_placeholder(self):
        return self.date_range_placeholder[self.language]


class ReportPageProgramControllerReports(MainNavigateButtons):
    lang_locator = {
        "programController_reports": {
            Language.eng: "ProgramController reports",
            Language.rus: "Отчеты ProgramController",
            Language.esp: "Reportes de ProgramController",
            "early_departures_from_work": {
                Language.eng: "Early departures from work",
                Language.rus: "Ранние уходы",
                Language.esp: "Salidas tempranas de trabajo",
            },
            "late_arrivals_work": {
                Language.eng: "Late arrivals at work",
                Language.rus: "Опоздания сотрудников",
                Language.esp: "Llegadas tardías a trabajo",
            },
            "worktime_log": {
                Language.eng: "Worktime log",
                Language.rus: "Журнал рабочего времени",
                Language.esp: "Registro de tiempo laboral",
            },
            "users_efficiency": {
                Language.eng: "Users efficiency",
                Language.rus: "Эффективность пользователей",
                Language.esp: "Eficiencia de usuarios",
            },
            "timesheet": {
                Language.eng: "Timesheet",
                Language.rus: "Табель рабочего времени",
                Language.esp: "Planilla horaria",
            },
            "total_time_user_work": {
                Language.eng: "Total time of user work",
                Language.rus: "Суммарное время работы пользователей",
                Language.esp: "Tiempo total de trabajo de usuarios",
            },
            "total_activity_processes": {
                Language.eng: "Total activity of processes",
                Language.rus: "Суммарная активность процессов",
                Language.esp: "Actividad total de procesos",
            },
            "total_activity_websites": {
                Language.eng: "Total activity of websites",
                Language.rus: "Суммарная активность сайтов",
                Language.esp: "Actividad total de sitios web",
            },
            "total_activity_processes_websites": {
                Language.eng: "Total activity of processes/websites",
                Language.rus: "Суммарная активность процессов/сайтов",
                Language.esp: "Actividad total de procesos/sitios web",
            },
        }
    }

    @property
    def programController_reports(self):
        return self.lang_locator["programController_reports"][self.language]

    @property
    def early_departures_from_work(self):
        return self.lang_locator["programController_reports"]["early_departures_from_work"][self.language]

    @property
    def late_arrivals_work(self):
        return self.lang_locator["programController_reports"]["late_arrivals_work"][self.language]

    @property
    def worktime_log(self):
        return self.lang_locator["programController_reports"]["worktime_log"][self.language]

    @property
    def users_efficiency(self):
        return self.lang_locator["programController_reports"]["users_efficiency"][self.language]

    @property
    def timesheet(self):
        return self.lang_locator["programController_reports"]["timesheet"][self.language]

    @property
    def total_time_user_work(self):
        return self.lang_locator["programController_reports"]["total_time_user_work"][self.language]

    @property
    def total_activity_processes(self):
        return self.lang_locator["programController_reports"]["total_activity_processes"][self.language]

    @property
    def total_activity_websites(self):
        return self.lang_locator["programController_reports"]["total_activity_websites"][self.language]

    @property
    def total_activity_processes_websites(self):
        return self.lang_locator["programController_reports"]["total_activity_processes_websites"][self.language]


class ReportPageSoftwareOnComputers(MainNavigateButtons):
    lang_locator = {
        "software_reports": {
            Language.eng: "Software reports",
            Language.rus: "Отчеты по программам",
            Language.esp: "Reportes de software",
            "software_on_computers": {
                Language.eng: "Software on computers",
                Language.rus: "Программы на компьютерах",
                Language.esp: "Software en computadoras",
                "dropdown_list_show": {
                    Language.eng: "Changes in software",
                    Language.rus: "Изменения программ",
                    Language.esp: "Cambios de software",
                },
                "first_date_range_placeholder": {
                    Language.eng: "dd.mm.yyyy",
                    Language.rus: "дд.мм.гггг",
                    Language.esp: "dd.mm.aaaa",
                },
            },
        }
    }

    @property
    def software_reports(self):
        return self.lang_locator["software_reports"][self.language]

    @property
    def software_on_computers(self):
        return self.lang_locator["software_reports"]["software_on_computers"][self.language]

    @property
    def dropdown_list_show(self):
        return self.lang_locator["software_reports"]["software_on_computers"]["dropdown_list_show"][self.language]

    @property
    def first_date_range_placeholder(self):
        return self.lang_locator["software_reports"]["software_on_computers"]["first_date_range_placeholder"][
            self.language
        ]


class ReportPageSystemReports(MainNavigateButtons):
    lang_locator = {
        "system_reports": {
            Language.eng: "System reports",
            Language.rus: "Системные отчеты",
            Language.esp: "Informes del sistema",
            "computers_inactive_active_agent": {
                Language.eng: "Computers with an inactive/active agent",
                Language.rus: "Компьютеры с неактивным/активным агентом",
                Language.esp: "Computadoras con un agente activo/inactivo",
            },
            "computers_without_agents": {
                Language.eng: "Computers without agents",
                Language.rus: "Компьютеры без агента",
                Language.esp: "Computadoras sin agentes",
            },
            "number_of_messages_computers": {
                Language.eng: "Number of messages by computers",
                Language.rus: "Количество сообщений по компьютерам",
                Language.esp: "Número de mensajes por computadora",
            },
        }
    }

    @property
    def system_reports(self):
        return self.lang_locator["system_reports"][self.language]

    @property
    def computers_inactive_active_agent(self):
        return self.lang_locator["system_reports"]["computers_inactive_active_agent"][self.language]

    @property
    def computers_without_agents(self):
        return self.lang_locator["system_reports"]["computers_without_agents"][self.language]

    @property
    def number_of_messages_computers(self):
        return self.lang_locator["system_reports"]["number_of_messages_computers"][self.language]


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
    }

    @property
    def connected_devices(self):
        return self.report_buttons["connected_devices"][self.language]

    @property
    def computer_devices(self):
        return self.report_buttons["computer_devices"][self.language]
