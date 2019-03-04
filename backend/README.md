# Brasa-pre

## Running locally

1. Create .env file

cd backend
end gabrielfior$ echo DATABASE_URL='"postgresql://localhost/brasa_pre5"' > .env

2. Create revision
cd backend
python manage.py db migrate -m "revision name"

To upgrade

python manage.py db upgrade

3. Run migration (make sure your database exists before) (make sure postgres is running locally)

cd backend
python manage.py db upgrade
 
4. Start app locally

cd backend
python app.py
