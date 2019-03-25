# Creating/updating models in the database

1. Update models
2. Create migration

```python
python backend/manage.py db migrate -m "my-cool-migration"
```

3. Upgrade head

```python
python backend/manage.py db upgrade head
```

* If needed, downgrade
```python
python backend/manage.py db downgrade
```


Reference:
- https://flask-migrate.readthedocs.io/en/latest/
