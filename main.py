from flask import Flask
from routes.gpt_routes import gpt_routes_bp

app = Flask(__name__)

# registering routes using Blueprint
app.register_blueprint(gpt_routes_bp)





