import pytest
from flask import Flask
from routes.gpt_routes import gpt_routes_bp


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(gpt_routes_bp)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

if __name__ == '__main__':
    pytest.main()