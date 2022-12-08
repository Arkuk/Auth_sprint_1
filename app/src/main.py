from flask import Flask
from db.postgres import db
from flask_migrate import Migrate
import models

app = Flask(__name__)
app.config.from_object('core.config.Settings')
migrate = Migrate(app, db)
db.init_app(app)

if __name__ == "__main__":
    app.run()
