from flask import Flask
from controllers.bike_controller.py import bike_bp

app = Flask(__name__)

# Registrar o Blueprint
app.register_blueprint(bike_bp)

if __name__ == '__main__':
    app.run(debug=True)
