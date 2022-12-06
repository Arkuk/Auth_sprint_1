from flask import Flask
from flask_migrate import Migrate
from db.postgres import db

app = Flask(__name__)

app.config.from_object('core.config.Settings')

migrate = Migrate(app, db)


@app.route('/hello-world')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
