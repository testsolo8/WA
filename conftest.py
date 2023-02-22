import os
import json
import logging
import pytest
from pytest import fixture
from playwright.sync_api import sync_playwright

from lang_locators import MainNavigateButtons, ReportNavigationButtons
from page_object.application import App


@fixture(scope="session", autouse=True)
def preconditionts():
    logging.info("preconditions started")
    yield
    logging.info("postconditions started")


@fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


# @fixture(scope="session", params=['firefox'])
@fixture(scope="session", params=["chromium"])
# @fixture(
#     scope="session",
#     params=["chromium", "webkit", "firefox"],
#     ids=["chromium", "webkit", "firefox"],
# )
def get_browser(get_playwright, request):
    browser = request.param
    headless = request.config.getini("headless")
    slow_mo = request.config.getini("slowmo")
    if headless == "True":
        headless = True
    else:
        headless = False
    if browser == "chromium":
        bro = get_playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
    elif browser == "firefox":
        bro = get_playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
    elif browser == "webkit":
        bro = get_playwright.webkit.launch(headless=headless, slow_mo=slow_mo)
    else:
        assert False, "unsupported browser type"
    yield bro
    bro.close()

@pytest.fixture(scope="session", params=["eng"])
# @pytest.fixture(scope="session", params=["eng", "esp", "rus"])
def lang_parametrize(request):
    return request.param


@pytest.fixture(scope="session")
def main_navigate_buttons(lang_parametrize):
    return MainNavigateButtons(lang_parametrize)


@pytest.fixture(scope="session")
def report_navigate_buttons(lang_parametrize):
    return ReportNavigationButtons(lang_parametrize)


@fixture(scope="session")
def desktop_app(main_navigate_buttons, get_browser, request):
    base_url = request.config.getoption("--base_url")
    ignore_https_errors = request.config.getoption("--ignore_https_errors")
    app = App(get_browser, ignore_https_errors=ignore_https_errors, base_url=base_url)
    app.trace()
    app.goto("/")
    app.choice_language(main_navigate_buttons.lang)
    yield app
    app.trace_stop()
    app.close()


@fixture(scope="session")
def desktop_app_auth(desktop_app, request):
    secure = request.config.getoption("--secure")
    config = load_config(secure)
    desktop_app.login(**config)
    yield desktop_app


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", help="base url of site under test", default="https://10.0.90.25"
    )
    parser.addini("headless", help="run browser in headless mode", default="")
    parser.addini("slowmo", help="run browser in slowmo mode", default=000)
    parser.addoption("--device", action="store", default="")
    parser.addoption("--browser", action="store", default="chromium")
    parser.addoption("--secure", action="store", default="secure.json")
    parser.addoption(
        "--ignore_https_errors",
        help="whether to ignore HTTPS errors when sending network requests",
        default=True,
    )


def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as cfg:
        return json.loads(cfg.read())
