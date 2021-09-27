from datetime import datetime
import pytz as pytz


def show_time():
    time_zone = pytz.timezone("Europe/Moscow")
    time = datetime.now(time_zone).strftime('%H:%M:%S')
    return time
