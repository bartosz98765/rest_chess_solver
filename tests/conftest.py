import pytest

from solver.rest_app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()
