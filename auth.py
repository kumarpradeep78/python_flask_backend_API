import jwt
from functools import wraps
from flask import request, jsonify
from config import Config
from datetime import datetime, timedelta

def generate_token():
    payload = {
        "user": "admin",
        "exp": datetime.now() + timedelta(hours=1)
    }
    return jwt.encode(payload, Config.JWT_SECRET, algorithm="HS256")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token missing"}), 401

        try:
            token = token.split(" ")[1]
            jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        except:
            return jsonify({"error": "Invalid or expired token"}), 401

        return f(*args, **kwargs)
    return decorated
