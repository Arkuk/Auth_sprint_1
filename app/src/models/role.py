from sqlalchemy.ext.associationproxy import association_proxy
from db.postgres import db
from models.mixins import (IdMixin,
                           CreatedTimeMixin,
                           UpdatedTimeMixin)


class Role(IdMixin, CreatedTimeMixin, UpdatedTimeMixin):
    __tablename__ = "role"

    name = db.Column(db.String(length=30), unique=True, nullable=False)
    associated_permissions = db.relationship("RolePermission")
    permissions = association_proxy("associated_permissions", "permission")
    associated_users = db.relationship("UserRole")
    users = association_proxy("associated_users", "user")


