import pytest
from config import bot, daily


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(daily, "Пора на дэйли https://telemost.yandex.ru/j/28259899709322022272839333735427715996")