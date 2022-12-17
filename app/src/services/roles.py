from db.postgres import db
from models.role import Role


class RoleService:
    def get_roles_list(self):
        """Получить список всех ролей сервиса"""
        roles = db.session.query(Role).all()
        return roles

    def create_role(self, body: dict):
        """Создание новой роли"""
        name = body['name']
        new_role = Role(name=name)
        db.session.add(new_role)
        db.session.commit()
        return new_role

    def delete_role(self, body: dict):
        """Удаление конкретной роли"""
        name = body['name']
        db.session.query(Role).filter_by(name=name).delete()
        db.session.commit()
        return f'role {name} deleted'


role_service = RoleService()
