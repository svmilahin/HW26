from app.database import db
from app.user.models import User


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey(User.id))
    executor_id = db.Column(db.Integer, db.ForeignKey(User.id))
    customer_user = db.relationship(User, foreign_keys=[customer_id])
    executor_user = db.relationship(User, foreign_keys=[executor_id])

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Order: {self.id}>'
