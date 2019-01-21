# Brasa Pre

[![CircleCI](https://circleci.com/gh/gabrielfior/brasa-pre/tree/master.svg?style=svg)](https://circleci.com/gh/gabrielfior/brasa-pre/tree/master)

### Starting app locally

Set environment variable APP_SETTINGS in a .env file in the src directory:
```dotenv
APP_SETTINGS="config.DevelopmentConfig"
```

To run from command-line:
```python
cd src
python app.py
```

Or to run locally with Heroku:
```heroku
heroku local web
```

### Running tests locally
```bash
pytest
```

Or to run a specific test:
```bash
pytest tests/test_database.py
```

### Adding a new model in database

1 - Add class to models.py file (add tablename, columns, relationships)
2 - Create migration by initialising the migrations directory once:

```bash
cd backend
python src/manage.py db revision -m "added region to cycle" --autogenerate
```

If any db operations need to be added, add manually to the .py file created inside the migrations folder.

The database in Heroku will execute the upgrade script when deploying upon release of a new version. If running locally, run:

```bash
python src/manage.py db upgrade
```

This will create tables and/or upgrade columns in the Postgres DB.

### Deploying to Heroku

git push heroku master

### Deployment to CircleCI

TBD

### Definition of done

- Code was written
- Tests were written
- CircleCI runs locally successfully
- Tests passed after submitting pull request
