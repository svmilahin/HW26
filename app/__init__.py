from flask import Flask

from .database import db
from config import DevelopmentConfig
import services


def create_app():

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()

        db.session.add_all([*services.users, *services.orders, *services.offers])
        db.session.commit()

    import app.user.views as usermodule
    import app.order.views as ordermodule
    import app.offer.views as offermodule

    app.register_blueprint(usermodule.module)
    app.register_blueprint(ordermodule.module)
    app.register_blueprint(offermodule.module)

    return app
