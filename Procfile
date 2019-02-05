web: gunicorn --pythonpath backend/ app:app
upgrade: python backend/src/manage.py db upgrade
release: bash release-tasks.sh