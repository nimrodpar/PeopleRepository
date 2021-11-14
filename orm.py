"""
    The layer that connects the model to the ORM.
    ORM specific (but easily replaceable).
"""

from sqlalchemy import (create_engine, Table)
from sqlalchemy.orm import (sessionmaker, registry)

import model

engine = create_engine('sqlite:///people.db', echo=False)  # can be switched out by any engine
Session = sessionmaker(engine)

mapper_registry = registry()

people = Table("people", mapper_registry.metadata, autoload_with=engine)

mapper_registry.map_imperatively(model.Person, people) # Maps the model to the table, easy peasy
