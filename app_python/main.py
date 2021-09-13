from flask import Flask, Response, send_file, request
from show_time import show_time
from prometheus_client import start_http_server, Counter, generate_latest, Gauge
import docker
import logging


def create_app(test_config=None):
    app = Flask(__name__)
    logger = logging.getLogger(__name__)

    CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
    MBFACTOR = float(1 << 20)

    memory_gauge = Gauge(
        'memory_usage_in_mb',
        'Amount of memory in megabytes currently in use by this container.',
        ['container_name']
    )
    requests_counter = Counter('num_requests', 'The number of requests.')

    client = docker.from_env(version='1.41')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route("/")
    def index():
        requests_counter.inc()
        return show_time()

    @app.route('/metrics', methods=['GET'])
    def get_data():
        """Returns all data as plaintext."""
        requests_counter.inc()

        containers = client.containers.list()

        # Get memory data for the container
        for container in containers:
            name = container.name
            try:
                with open('/docker/memory/{}/memory.usage_in_bytes'.format(container.id), 'r') as memfile:
                    memory = memfile.read()
                    memory = int(memory) / MBFACTOR
                    memory_gauge.labels(name).set(memory)
            except Exception as e:
                logger.error("Failed to update memory metric. Exception: {}".format(e))

        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0")
