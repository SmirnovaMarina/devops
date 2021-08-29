from datetime import datetime
import pytz as pytz
from flask import render_template


def show_time():
    time_zone = pytz.timezone("Europe/Moscow")
    time = datetime.now(time_zone).strftime('%H:%M:%S')
    return render_template('index.html', time=time)
