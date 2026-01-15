from flask import Flask, jsonify
from config import Config
from models import db
from routes import employee_bp
from auth import generate_token

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(employee_bp)

@app.route("/login", methods=["POST"])
def login():
    return jsonify({"token": generate_token()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
