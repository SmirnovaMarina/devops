import re


def test_show_time(client):
    response = client.get('/')
    regex = (r'[0-9]{2}:[0-9]{2}:[0-9]{2}')
    assert re.search(regex, response.data.__str__()) is not None
