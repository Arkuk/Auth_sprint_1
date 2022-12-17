docker compose up -d
flask db init
flask db migrate
flask db upgrade
flask create-roles
flask createsuperuser admin 123