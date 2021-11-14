# People Repository

A simple example for having persistent objects in python using the Repository pattern in a way that is decoupled from the ORM.

## Setup
```bash
pip install -r requirements.txt
python people_repository/manage.py version_control sqlite:///people.db people_repository  # setup db
python manage.py upgrade  # run migrations
```
