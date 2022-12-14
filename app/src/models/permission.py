# from db.postgres import db
# from models.mixins import (IdMixin,
#                            CreatedTimeMixin,
#                            UpdatedTimeMixin)
#
#
# class Permission(IdMixin, CreatedTimeMixin, UpdatedTimeMixin):
#     __tablename__ = "permission"
#
#     name = db.Column(db.String(length=30), unique=True, nullable=False)
