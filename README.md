# People Repository

A simple example for having persistent objects in python using the Repository pattern in a way that is decoupled from the ORM.

Note: For completeness, the repository includes migrations which are heavily coupled with `sqlalchemy`. These can be replace by any ORM and migration manager (however the `sqlalchemy-migrate` one is really nice).

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
from datetime import date


r = PeopleRepository()

r.add(Person(1337, "Mike", date(2000, 1, 31), "IL"))

assert not r.get(1)

p = r.get(1337)
assert p.name == "Mike"
```
