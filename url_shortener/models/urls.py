from typing_extensions import Self

from models import db


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visits = db.Column(db.Integer, default=0)
    shortened = db.Column(db.String(10))
    url = db.Column(db.String(200), nullable=False)

    @classmethod
    def find_by_shortened(cls, shortened: str) -> Self:
        return cls.query.filter(cls.shortened.contains(shortened)).first()

    @classmethod
    def find_by_url(cls, url: str) -> Self:
        return cls.query.filter_by(url=url).first()

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "url": self.url,
            "shortened": self.shortened,
            "number_of_visits": self.visits,
        }

    def save_to_db(self) -> Self:
        db.session.add(self)
        db.session.commit()
        return self
