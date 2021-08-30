from flask import Flask
from show_time import show_time


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route("/")
    def index():
        return show_time()

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0")
