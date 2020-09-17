import os
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.local import LocalProxy

logger = LocalProxy(lambda: app.logger)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
