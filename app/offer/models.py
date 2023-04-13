from app.database import db
from app.user.models import User
from app.order.models import Order


class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id))
    executor_id = db.Column(db.Integer, db.ForeignKey(User.id))

    order = db.relationship(Order)
    executor = db.relationship(User)

    def __str__(self):
        return f'{self.id} {self.user.last_name}'

    def __repr__(self):
        return f'<Offer: {self.id}>'
