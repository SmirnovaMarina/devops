def test_template_sentence(client):
    response = client.get('/')
    assert b'The current time in Moscow is:' in response.data
