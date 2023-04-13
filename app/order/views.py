from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app.database import db
from .models import Order


module = Blueprint('orders', __name__, url_prefix='/orders')


@module.get('/')
def user():
    try:
        orders = Order.query.all()
        if orders is None:
            return 'Нет заказов!'

        return jsonify(
            [{
            'id': order.id,
            'name': order.name,
            'description': order.description,
            'start_date': order.start_date,
            'end_date': order.end_date,
            'address': order.address,
            'price': order.price,
            'customer_id': order.customer_id,
            'executor_id': order.executor_id,
            } for order in orders]), 200
    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.get('<int:pk>')
def order_get(pk):
    try:
        order = Order.query.get(pk)
        if order is None:
            return 'Нет заказа!'

        return jsonify({'id': order.id,
            'name': order.name,
            'description': order.description,
            'start_date': order.start_date,
            'end_date': order.end_date,
            'address': order.address,
            'price': order.price,
            'customer_id': order.customer_id,
            'executor_id': order.executor_id,}), 200

    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.post('/')
def order_add():
    try:
        order_new = Order(**request.json)
        db.session.add(order_new)
        db.session.commit()
        return 'Запись была успешно добавлена!', 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.put('<int:pk>')
def order_updata_pk(pk):
    try:
        data = request.json
        order = Order.query.get(pk)
        if order is None:
            return 'Нет заказа!'
        order.name = data['name']
        order.description = data['description']
        order.start_date = data['start_date']
        order.end_date = data['end_date']
        order.address = data['address']
        order.price = data['price']
        order.customer_id = data['customer_id']
        order.executor_id = data['executor_id']
        db.session.add(order)
        db.session.commit()
        return 'Заказ был успешно обновлен!', 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.delete('<int:pk>')
def order_delete_pk(pk):
    try:
        order = Order.query.get(pk)
        if order is None:
            return 'Нет заказа!'

        db.session.delete(order)
        db.session.commit()
        return 'Заказ был успешно удален!', 204
    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500
