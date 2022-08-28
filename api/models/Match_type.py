from api.core import Mixin
from .base import db


class MatchType(Mixin, db.Model):
    """Match Type Table."""

    __tablename__ = "Match_type"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    match_type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<MatchType {self.match_type}>"
