import pytest
from config import bot, daily_main
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
    bot.send_message(daily_main, "Пора на дэйли https://us06web.zoom.us/j/89233765337?pwd=akr7biplJEpGIIeWxbHbc29W3yMg13.1")
    if cat_result:
        bot.send_photo(daily_main, cat_result)