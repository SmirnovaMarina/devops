from datetime import datetime
import pytz as pytz


def test_show_time(client):
    response = client.get('/')
    time_zone = pytz.timezone("Europe/Moscow")
    time = datetime.now(time_zone).strftime('%H:%M:%S')
    assert time.encode() in response.data
