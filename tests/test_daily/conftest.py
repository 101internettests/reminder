import pytest
from config import bot, daily_main


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(daily_main, "Пора на дэйли https://us06web.zoom.us/j/89233765337?pwd=akr7biplJEpGIIeWxbHbc29W3yMg13.1")