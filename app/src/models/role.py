from db.postgres import db
from models.mixins import (IdMixin,
                           CreatedTimeMixin,
                           UpdatedTimeMixin)
from models.permission import Permission
from models.role_permission import role_permission


class Role(IdMixin, CreatedTimeMixin, UpdatedTimeMixin):
    __tablename__ = "role"
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    roles = db.relationship(Permission, secondary=role_permission, backref='permission')
