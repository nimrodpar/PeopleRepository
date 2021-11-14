"""
    A pure data model for the problem domain.
    Decoupled from the underlying ORM.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    idn: int
    name: str
    birth_date: datetime
    nationality: str

    def __init__(self, idn: int, name: str, birth_date: datetime, nationality: str) -> None:
        self.idn = idn
        self.name = name
        self.birth_date = birth_date
        self.nationality = nationality
