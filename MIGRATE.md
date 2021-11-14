# Migrations HOWTO

Note: The `migrate` command becomes available once `sqlalchemy-migrate` is installed.

```bash
migrate create people_repository "People Repository"  # creates an initially empty repository to handle migrations
python people_repository/manage.py version_control sqlite:///people.db people_repository  # The version_control command assigns a specified database with a repository
python people_repository/manage.py db_version sqlite:///people.db people_repository # read the version
```
Create the `manage.py` script to replace the explicit calling to `migrate`:
```bash
migrate manage manage.py --repository=people_repository --url=sqlite:///people.db
python manage.py db_version # read the version
```

To create a migration script:
```bash
python manage.py script "lowercase name for migration"
```

To run migrations:
```bash
python manage.py upgrade (<version number>)
python manage.py downgrade <version number>
```