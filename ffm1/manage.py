# manage.py
import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from project.server import app, db, models


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port='8000'))
# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


if __name__ == '__main__':
    db.create_all()
    manager.run()
