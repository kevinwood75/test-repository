from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')  # The lazy option does not create a object for every row


    def __init__(self,name):
        self.name = name


    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}   # need to use .all() when using "lazy=dynamic"

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name , returns an ITEM model object

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()