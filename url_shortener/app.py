import os
from typing import Union

from flask import Flask, request
from hashids import Hashids

from models.urls import db, Urls


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

hashids = Hashids(salt=os.getenv("SALT", "supersecretsalt"), min_length=6)


@app.before_first_request
def create_db():
    db.create_all()


@app.route("/<string:shortened>")
def index(shortened: str) -> Union[dict, str]:
    if match := Urls.find_by_shortened(shortened):
        match.visits += 1
        match.save_to_db()
        return match.to_json()["url"]
    return {"msg": "No such URL"}, 404


@app.route("/urls/shorten", methods=["POST"])
def shorten() -> dict:
    try:
        url = request.get_json()["url"]
    except KeyError:
        return {"msg": "Error"}, 404
    if match := Urls.find_by_url(url):
        return {"original": url, "shortened": match.shortened}

    new_url = Urls(url=url).save_to_db()
    new_url.shortened = f"http://127.0.0.1:8000/{hashids.encode(new_url.id)}"  # localhost testing
    # new_url.shortened = f"http://tier.app/{hashids.encode(new_url.id)}"
    new_url.save_to_db()
    return {"original": url, "shortened": new_url.shortened}


@app.route("/urls")
def stats() -> dict:
    return {"urls": [url.to_json() for url in Urls.query.all()]}


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=8000, debug=True)
