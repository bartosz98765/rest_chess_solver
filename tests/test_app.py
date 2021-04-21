def test_moves(client):
    # correct query (king)
    assert client.get('/api/v1/king/a1').status_code == 200
    # invalid field
    response = client.get('/api/v1/king/invalid_field')
    assert response.status_code == 409
    assert response.get_json()['error'] == "Field does not exist."
    # invalid figure
    response = client.get('/api/v1/invalid_figure/a1')
    assert response.status_code == 404
    assert response.get_json()['error'] == "Figure does not exist."


def test_validation(client):
    # correct KING move
    assert client.get('/api/v1/king/a1/a2').status_code == 200
    # invalid field
    response = client.get('/api/v1/king/a1/invalid_field')
    assert response.status_code == 409
    assert response.get_json()['error'] == "Field does not exist."
    # invalid figure
    response = client.get('/api/v1/invalid_figure/a1/a2')
    assert response.status_code == 404
    assert response.get_json()['error'] == "Figure does not exist."
    # incorrect KING move
    response = client.get('/api/v1/king/a1/a3')
    assert response.status_code == 200
    assert response.get_json()['error'] == "Current move is not permitted"
