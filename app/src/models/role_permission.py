# import uuid
#
# from sqlalchemy.dialects.postgresql import UUID
# from db.postgres import db
#
# role_permission = db.Table(
#     'role_permission',
#     db.Column('id',
#               UUID(as_uuid=True),
#               primary_key=True,
#               default=uuid.uuid4,
#               unique=True,
#               nullable=False,
#               ),
#     db.Column('role_id', db.ForeignKey('role.id')),
#     db.Column('permission_id', db.ForeignKey('permission.id')),
# )
