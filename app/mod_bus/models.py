from app import db

class Bus(db.Model):
    __tablename__ = 'buses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    city_id = db.Column(db.Integer)

    def __init__(self, name, description, city_id):
        self.name = name
        self.description = description
        self.city_id = city_id