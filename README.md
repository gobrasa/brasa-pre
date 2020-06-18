# Brasa Pre

[![CircleCI](https://circleci.com/gh/gabrielfior/brasa-pre/tree/master.svg?style=svg)](https://circleci.com/gh/gabrielfior/brasa-pre/tree/master)

### Starting app locally


To run from command-line:
```python
cd backend
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

* Add class to models.py file (add tablename, columns, relationships)

* Create .env file

```
cd backend 
echo DATABASE_URL='"postgresql://localhost/brasa_pre5"' > .env
```

* Create migration by initialising the migrations directory once:

```bash
cd backend
python backend/manage.py db migrate -m "created initial tables"
```

If any db operations need to be added, add manually to the .py file created inside the migrations folder.

The database in Heroku will execute the upgrade script when deploying upon release of a new version. If running locally, run:

```bash
python backend/manage.py db upgrade
```

This will create tables and/or upgrade columns in the Postgres DB.


### Deploying to Heroku

git push heroku master

### Deployment to CircleCI

TBD
