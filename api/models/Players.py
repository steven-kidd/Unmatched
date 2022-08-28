from api.core import Mixin
from .base import db


class Player(Mixin, db.Model):
    """Player Table."""

    __tablename__ = "Players"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Player {self.name}>"
