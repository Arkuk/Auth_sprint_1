from main import ma
from models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "username")
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)
