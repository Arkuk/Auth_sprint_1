from sqlalchemy.dialects.postgresql import UUID

from db.postgres import db
from models.mixins import (IdMixin,
                           CreatedTimeMixin
                           )


class UserRole(IdMixin, CreatedTimeMixin):
    __tablename__ = "user_role"
    __table_args__ = (db.UniqueConstraint("user_id", "permission_id"),)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"))
    permission_id = db.Column(UUID(as_uuid=True), db.ForeignKey("permission.id"))

    user = db.relationship("User")
    role = db.relationship("Role")
