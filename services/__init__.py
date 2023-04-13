from utils import Data
from config import BASE_DIR
from app.user.models import User
from app.order.models import Order
from app.offer.models import Offer

users_ = Data(f'{BASE_DIR}/data/users.json').load_data()
orders_ = Data(f'{BASE_DIR}/data/orders.json').load_data()
offers_ = Data(f'{BASE_DIR}/data/offers.json').load_data()

users = [User(**data) for data in users_]
orders = [Order(**data) for data in orders_]
offers = [Offer(**data) for data in offers_]
