web: gunicorn --pythonpath backend/src app:app
init: python backend/src/manage.py db init
migrate: python backend/src/manage.py db migrate
upgrade: python backend/src/manage.py db upgrade
release: ./release-tasks.sh