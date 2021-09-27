import os
from flask import Blueprint, Flask, Response, \
    render_template  # ,send_file, request
from show_time import show_time
from prometheus_client import Counter, \
    generate_latest, Gauge  # ,start_http_server,
import docker
import logging
from multiprocessing import Value


MAIN = Blueprint("main", __name__)
logger = logging.getLogger(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
MBFACTOR = float(1 << 20)

memory_gauge = Gauge(
    'memory_usage_in_mb',
    'Amount of memory in megabytes currently in use by this container.',
    ['container_name']
)
requests_counter = Counter('num_requests', 'The number of requests.')

counter = Value('i', 0)

client = docker.from_env(version='1.41')

os.mkdir('./files')


@MAIN.route('/')
def index():
    requests_counter.inc()
    counter.value += 1
    time = show_time()

    file = open('files/visits.txt', 'a+')
    file.write('{}\n'.format(time))
    file.close()

    return render_template('index.html', time=time)


@MAIN.route('/visits')
def get_requests_number():
    file = open('files/visits.txt', 'r')
    contents = file.read()
    file.close()
    return 'The number of visits is {}.\n' \
           'Content: {}'.format(counter.value, contents)


@MAIN.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""

    containers = client.containers.list()

    # Get memory data for the container
    for container in containers:
        name = container.name
        try:
            with open(''
                      '/docker/memory/{}/'
                      'memory.usage_in_bytes'.format(container.id),
                      'r') as memfile:
                memory = memfile.read()
                memory = int(memory) / MBFACTOR
                memory_gauge.labels(name).set(memory)
        except Exception as e:
            logger.error("Failed to "
                         "update memory metric. Exception: {}".format(e))

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(MAIN)

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0")
