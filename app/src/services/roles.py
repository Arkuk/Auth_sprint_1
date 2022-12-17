from db.postgres import db
from flask_restx import abort
from flask_restx._http import HTTPStatus

from models.role import Role
from models.user_role import user_role


class RoleService:
    def get_roles_list(self):
        """Получить список всех ролей сервиса"""
        roles = db.session.query(Role).all()
        return roles

    def create_role(self, body: dict):
        """Создание новой роли, если роль уже существует, вернется сообщение об ошибке"""
        name = body['name']
        role = db.session.query(Role).filter_by(name=name).all()
        if not role:
            new_role = Role(name=name)
            db.session.add(new_role)
            db.session.commit()
            return new_role
        else:
            abort(HTTPStatus.CONFLICT, 'Role is already exist')

    def update_role(self, body: dict):
        """Изменить название роли"""
        role_id = body['id']
        name = body['name']
        role = db.session.query(Role).filter_by(id=role_id).one()
        print(role)
        if role:
            role.name = name
            db.session.commit()
            return role
        else:
            abort(HTTPStatus.CONFLICT, 'No role to update')

    def delete_role(self, body: dict):
        """Удаление конкретной роли, если роль присвоена какому-либо пользователю, получим сообщение об ошибке"""
        role_id = body['id']
        query = user_role.select().where(user_role.c.role_id == role_id)
        role_with_user = db.session.execute(query).all()
        if not role_with_user:
            db.session.query(Role).filter_by(id=role_id).delete()
            db.session.commit()
            return f'role {role_id} deleted'
        else:
            abort(HTTPStatus.CONFLICT, 'Have users with the role, role cannot be deleted')


role_service = RoleService()
