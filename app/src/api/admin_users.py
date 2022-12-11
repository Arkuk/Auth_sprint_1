from flask_restx import Namespace, Resource

api = Namespace('API для управления доступами. Юзеры')


@api.route('/users')
class User(Resource):

    def get(self):
        pass
