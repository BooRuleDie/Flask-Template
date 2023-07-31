from flask import Flask
from blueprints.base_routes import base_routes
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32) 
app.static_folder = "blueprints/static"
app.template_folder = "blueprints/templates"

app.register_blueprint(base_routes)

if __name__ == '__main__':
    app.run(debug=True)
