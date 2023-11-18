from app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wikiDataId = db.Column(db.String(100))
    ctype = db.Column(db.String(50))
    city = db.Column(db.String(100))
    name = db.Column(db.String(100))
    country = db.Column(db.String(100))
    countryCode = db.Column(db.String(10))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    currency_code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    wiki_data_id = db.Column(db.String(20))
