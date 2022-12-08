from sqlalchemy.ext.associationproxy import association_proxy
from db.postgres import db
from models.mixins import (IdMixin,
                           CreatedTimeMixin,
                           UpdatedTimeMixin)


class User(IdMixin, CreatedTimeMixin, UpdatedTimeMixin):
    __tablename__ = 'user'

    username = db.Column(
        db.String(length=56), unique=True, nullable=False
    )
    password = db.Column(db.String(length=256), nullable=False)
    associated_roles = db.relationship("UserRole")
    roles = association_proxy("associated_roles", "role")
