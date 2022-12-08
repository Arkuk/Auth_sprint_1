from sqlalchemy.orm import relationship

from db.postgres import db
from models.mixins import (IdMixin,
                           CreatedTimeMixin,
                           UpdatedTimeMixin)


class Role(IdMixin, CreatedTimeMixin, UpdatedTimeMixin):
    __tablename__ = "role"

    name = db.Column(db.String(length=30), unique=True, nullable=False)