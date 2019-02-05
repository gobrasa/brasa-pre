web: gunicorn --pythonpath backend/ -b :$PORT app:app
upgrade: python backend/src/manage.py db upgrade
release: bash release-tasks.sh