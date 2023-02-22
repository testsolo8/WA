from conftest import load_config


def test_login_page(desktop_app):
    assert desktop_app.login_page.check_login_page_exists() == "WebAnalytic"


def test_login_page_auth(desktop_app, request):
    secure = request.config.getoption("--secure")
    config = load_config(secure)
    desktop_app.login(**config)
    assert desktop_app.login_page.check_login_page_auth_ok() == "Search"
