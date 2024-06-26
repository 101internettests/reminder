import pytest
from config import bot, daily
import requests

cats_url: str = 'https://api.thecatapi.com/v1/images/search'


def cat_picture(url):
    cats_req = requests.get(url)
    if cats_req.status_code == 200:
       return cats_req.json()[0]['url']
    else:
        return None


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    cat_result = cat_picture(cats_url)
    bot.send_message(daily, "Пора на дэйли https://telemost.yandex.ru/j/28259899709322022272839333735427715996")
    if cat_result:
        bot.send_photo(daily, cat_result)

