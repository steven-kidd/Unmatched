from flask import Blueprint, request
from api.models import db, Match, Player
from api.core import create_response, serialize_list, logger
from sqlalchemy import inspect

main = Blueprint("main", __name__)  # initialize blueprint


# function that is called when you visit /
@main.route("/health")
def health():
    # you are now in the current application context with the main.route decorator
    # access the logger with the logger from api.core and uses the standard logging module
    # try using ipdb here :) you can inject yourself
    logger.info("Hello World!")
    return create_response()


# function that is called when you visit /players
@main.route("/players", methods=["GET"])
def get_players():
    players = Player.query.all()
    return create_response(data={"players": serialize_list(players)})


# POST request for /players
@main.route("/players", methods=["POST"])
def create_player():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "name" not in data:
        msg = "No name provided for player."
        logger.info(msg)
        return create_response(status=422, message=msg)
    if "email" not in data:
        msg = "No email provided for player."
        logger.info(msg)
        return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    new_person = Player(name=data["name"], email=data["email"])

    # commit it to database
    db.session.add_all([new_person])
    db.session.commit()
    return create_response(
        message=f"Successfully created person {new_person.name} with id: {new_person.id}"
    )