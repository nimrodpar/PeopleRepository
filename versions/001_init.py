from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime

meta = MetaData()


people = Table(
    "people", meta,
    Column("idn", Integer, primary_key=True),  # TODO: test set autoincrement=True and add without an id
    Column("name", String(255), nullable=False),
    Column("birth_date", DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    people.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    people.drop()
