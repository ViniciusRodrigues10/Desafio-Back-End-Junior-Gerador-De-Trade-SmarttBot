import mongoengine

class Trade(mongoengine.Document):
    asset = mongoengine.StringField()
    price = mongoengine.FloatField()
    date = mongoengine.StringField()