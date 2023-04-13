from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app.database import db
from .models import Offer


module = Blueprint('offers', __name__, url_prefix='/offers')


@module.get('/')
def offers():
    try:
        offers = Offer.query.all()
        if offers is None:
            return 'Нет предложений!'

        return jsonify(
            [{'id': offer.id,
            'order_id': offer.order_id,
            'executor_id': offer.executor_id} for offer in offers]), 200

    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.get('<int:pk>')
def offer_get(pk):
    try:
        offer = Offer.query.get(pk)
        if offer is None:
            return 'Нет предложения!'

        return jsonify({'id': offer.id,
            'order_id': offer.order_id,
            'executor_id': offer.executor_id}), 200

    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.post('/')
def offer_add():
    try:
        offer_new = Offer(**request.json)
        db.session.add(offer_new)
        db.session.commit()
        return 'Запись была успешно добавлена!', 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.put('<int:pk>')
def offer_updata_pk(pk):
    try:
        data = request.json
        offer = Offer.query.get(pk)
        if offer is None:
            return 'Нет предложения!'
        offer.customer_id = data['order_id']
        offer.executor_id = data['executor_id']
        db.session.add(offer)
        db.session.commit()
        return 'Предложение был успешно обновлено!', 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.delete('<int:pk>')
def offer_delete_pk(pk):
    try:
        offer = Offer.query.get(pk)
        if offer is None:
            return 'Нет предложения!'

        db.session.delete(offer)
        db.session.commit()
        return 'Предложение былы успешно удалено!', 204
    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500
