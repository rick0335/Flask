from app import app
from flask import jsonify

data = [
    {"id": 0,
    "lastName": "Funk Jørgensen",
    "firstName": "Ricki"},

    {"id": 1,
    "lastName": "Østergaard Andersen",
    "firstName": "Mie"}
]


@app.route("/api/", methods=["GET"])
def home():
    return \
    "<h2>Endpoints</h2>"\
    "<p>api/users/</p>"\
    "<p>api/users/id</p>";

@app.route("/api/users/", methods=["GET"])
def users():
    return jsonify(data);

@app.route("/api/users/<int:id>/", methods=["GET"])
def user(id):
    return jsonify(data[id]);