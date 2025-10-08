#!/usr/bin/env python3

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "MY_SECRET_KEY"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Password Auth

auth = HTTPBasicAuth()
@auth.verify_password
def verify_password(u, p):
    if u in users and check_password_hash(users[u]["password"], p):
        return u

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Token Auth
@app.route("/login", methods=["POST"])
def login():
    u = request.json.get("username")
    p = request.json.get("password")
    if verify_password(u, p):
        access_token = create_access_token(identity=u)
        return {"access_token": access_token}
    return "", 401
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    if users[username]["role"] != "admin":
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run()
