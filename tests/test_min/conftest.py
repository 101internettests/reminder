import pytest
from config import bot, daily


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(daily, "Доброе утро! Напоминаю: через 10 минут у нас созвон.")