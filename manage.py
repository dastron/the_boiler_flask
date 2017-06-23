import os
from flask_script import Manager, Server, prompt_bool
from the_boiler.webapp import app, database, setup_app

manager = Manager(app)

api = setup_app(os.getenv('BOILER_CONFIG', 'default'), app, database)


manager.add_command('runlocal', Server(host='localhost', port=5000))


@manager.shell
def make_shell_context():
    """This saves quite a few imports."""
    return dict(app=app, db=database, api=api)


@manager.command
def init_db():
    """Initializes the database."""

    # from the_boiler.models import Program
    print os.getenv('BOILER_CONFIG', 'default')
    if prompt_bool('You sure you wanna create (recreate) the current tables?'):
        database.drop_all()
        database.create_all()
    else:
        database.create_all()


@manager.command
def create_tables():
    """Drops all the tables."""
    if prompt_bool('You sure you wanna create tables?'):
        database.create_all()


@manager.command
def drop_tables():
    """Drops all the tables."""
    print os.getenv('BOILER_CONFIG', 'default')
    if prompt_bool('You sure you wanna destroy everything?'):
        database.drop_all()


if __name__ == '__main__':
    manager.run()
