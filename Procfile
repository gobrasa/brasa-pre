web: gunicorn --pythonpath backend/ -b 0.0.0.0:$PORT app:app
upgrade: python backend/src/manage.py db upgrade
release: bash release-tasks.sh