from flask import Blueprint, jsonify, abort, request
from sqlalchemy.exc import SQLAlchemyError

from app.database import db
from .models import User


module = Blueprint('users', __name__, url_prefix='/users')


@module.get('/')
def user():
    try:
        users = User.query.all()
        if users is None:
            return 'Нет пользователей!'

        return jsonify(
            [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age,
            'email': user.email,
            'role': user.role,
            'phone': user.phone} for user in users]), 200
    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.get('<int:pk>')
def user_get(pk):
    try:
        user = User.query.get(pk)
        if user is None:
            return 'Нет пользовател!'

        return jsonify({'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age,
                'email': user.email,
                'role': user.role,
                'phone': user.phone}), 200

    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.post('/')
def user_add():
    try:
        user_new = User(**request.json)
        db.session.add(user_new)
        db.session.commit()
        return 'Запись была успешно добавлена!', 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.put('<int:pk>')
def user_updata_pk(pk):
    try:
        data = request.json
        user = User.query.get(pk)
        if user is None:
            return 'Нет пользователя!'
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.age = data['age']
        user.email = data['email']
        user.role = data['role']
        user.phone = data['phone']
        db.session.add(user)
        db.session.commit()
        return 'Пользователь был успешно обновлен!', 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500


@module.delete('<int:pk>')
def user_delete_pk(pk):
    try:
        user = User.query.get(pk)
        if user is None:
            return 'Нет пользователя!'

        db.session.delete(user)
        db.session.commit()
        return 'Пользователь был успешно удален!', 204
    except SQLAlchemyError as e:
        return f'Произошла непредвиденная ошибка во время запроса к базе данных {e}', 500
