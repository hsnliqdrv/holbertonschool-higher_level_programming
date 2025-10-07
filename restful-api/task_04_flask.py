#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"
users = {}
@app.route("/data")
def data():
    return list(users.keys())
@app.route("/status")
def status():
    return "OK"
@app.route("/users/<username>")
def user(username):
    if username in users:
        return jsonify(users[username])
    return {"error": "User not found"}, 404
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if "username" in data:
        users[data["username"]] = data
        return {"message": "User added",
                "user": data}, 201
    return {"error":"Username is required"}, 400

if __name__ == "__main__":
    app.run(debug=True)
