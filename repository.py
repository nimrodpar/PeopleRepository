"""
    A get()/add() repository for persistently saving people.
"""

import model
import orm


class PeopleRepository:
    def __init__(self):
        self.session = orm.Session()

    def add(self, person: model.Person):
        if self.get(person.idn):
            print(f"Person with id {person.idn} already in Repository.")
            return
        self.session.add(person)
        self.session.commit()

    def delete(self, idn: int):
        self.session.query(model.Person).filter_by(idn=idn).delete()
        self.session.commit()

    def get(self, idn: int) -> model.Person:
        return self.session.query(model.Person).filter_by(idn=idn).one_or_none()

    def list(self):
        return self.session.query(model.Person).all()
