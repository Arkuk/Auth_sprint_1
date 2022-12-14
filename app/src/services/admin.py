from db.postgres import db
from models.user import User

class AdminService:
    def get_list_data(self):
        users = db.session.execute(db.select(User)).all()
        return users

    def edit_data(self):
        pass

admin_service = AdminService()