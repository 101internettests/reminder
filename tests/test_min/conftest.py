import pytest
from config import bot, daily_main


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(daily_main, "Доброе утро! Напоминаю: через 10 минут у нас созвон.")