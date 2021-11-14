from sqlalchemy import Table, MetaData, String, Column


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    people = Table('people', meta, autoload=True)
    nationality = Column('nationality', String(2))  # country code
    nationality.create(people)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    people = Table('people', meta, autoload=True)
    people.c.nationality.drop()
