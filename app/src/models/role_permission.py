from sqlalchemy.dialects.postgresql import UUID
from db.postgres import db
from models.mixins import (IdMixin,
                           CreatedTimeMixin
                           )


class RolePermission(IdMixin, CreatedTimeMixin):
    __tablename__ = "role_permission"
    __table_args__ = (db.UniqueConstraint("role_id", "permission_id"),)

    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey("role.id"))
    permission_id = db.Column(UUID(as_uuid=True), db.ForeignKey("permission.id"))
