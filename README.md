# People Repository

A simple example for having persistent objects in python using the Repository pattern in a way that is decoupled from the ORM.

## Setup
```bash
pip install -r requirements.txt
python people_repository/manage.py version_control sqlite:///people.db people_repository  # setup db
migrate manage manage.py --repository=people_repository --url=sqlite:///people.db  # create manage.py
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
