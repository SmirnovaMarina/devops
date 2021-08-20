import pytz as pytz
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return show_time()

def show_time():
    time_zone = pytz.timezone("Europe/Moscow")
    time = datetime.now(time_zone).strftime('%H:%M:%S')
    return render_template('index.html', time=time)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
