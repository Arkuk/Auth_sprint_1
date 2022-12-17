from db.postgres import db
from models.user_role import user_role
from models.user import User
from models.role import Role


class UserRoles:

    def get_user_roles(self, user_id):
        """Получить список ролей конкретного пользователя"""
        query = user_role.select().where(user_role.c.user_id == user_id)
        roles_id = db.session.execute(query).all()
        #roles_id = db.session.execute(db.select(user_role).filter_by(user_id=user_id)).all()
        return roles_id

    def assign_role(self, user_id, body: dict):
        """Присвоение роли конкретному пользователю"""
        role_id = body['role_id']
        role_user = user_role.insert().values(user_id=user_id, role_id=role_id)
        db.session.execute(role_user)
        db.session.commit()
        return role_user

    def discard_role(self, user_id, body: dict):
        """Удаление роли у пользователя"""
        role_id = body['role_id']
        role = user_role.select().with_only_columns([user_role.c.id]).where(user_role.c.role_id == role_id and
                                                                            user_role.c.user_id == user_id)
        role = db.session.execute(role).first()
        delete_role = user_role.delete().where(user_role.c.id == role[0])
        db.session.execute(delete_role)
        db.session.commit()
        return role[0]

user_roles = UserRoles()
