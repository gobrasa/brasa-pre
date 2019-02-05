# Brasa-pre

## Running locally

1. Create .env file

cd backend
end gabrielfior$ echo DATABASE_URL='"postgresql://localhost/brasa_pre5"' > .env

2. Run migration (make sure your database exists before) (make sure postgres is running locally)

cd backend
python manage.py db upgrade
 
3. Start app locally

cd backend
python app.py

## Database

### How to create mentees

Each mentee has a username and a mentor_id. Therefore you need to create mentors before creating mentees.

Then create a mentee and pass the mentor_id.

### How to create mentors

First create a username. Then create a cycle. Then create a mentor to that cycle and to that username.