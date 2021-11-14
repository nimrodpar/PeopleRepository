# People Repository

A simple example for having persistent objects in python using the Repository pattern in a way that is decoupled from the ORM.

## Setup
```bash
pip install -r requirements.txt
migrate create people_repository "People Repository"
mv versions people_repository/versions
python people_repository/manage.py version_control sqlite:///people.db people_repository  # setup db
python manage.py upgrade  # run migrations
```

## Usage

```python
from repository import PeopleRepository
from model import Person
from datetime import datetime

rp = PeopleRepository()

rp.add(Person(1, "Mike", datetime.now(), "IL"))

p = rp.get(1)

assert p.name == "Mike"
```
