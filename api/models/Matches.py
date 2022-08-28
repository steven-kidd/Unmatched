from api.core import Mixin
from .base import db


class Match(Mixin, db.Model):
    """Match Table."""

    __tablename__ = "Matches"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    match_type = db.Column(db.Integer, db.ForeignKey("Match_type.id"), nullable=True)
    Player1_ID = db.Column(db.Integer, db.ForeignKey("Players.id"), nullable=False)
    Player2_ID = db.Column(db.Integer, db.ForeignKey("Players.id"), nullable=False)
    Player3_ID = db.Column(db.Integer, db.ForeignKey("Players.id"), nullable=True)
    Player4_ID = db.Column(db.Integer, db.ForeignKey("Players.id"), nullable=True)
    Winner1_ID = db.Column(db.Integer, db.ForeignKey("Players.id"), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Player {self.name}>"
