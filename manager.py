from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Community, Reports, Recommends, Comments

# Creating the app instance
# app = create_app('dev')
# app = create_app('test')
app = create_app('prod')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """
    Running the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.Text.TestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                Community=Community,
                Reports=Reports,
                Recommends=Recommends,
                Comments=Comments)


if __name__ == '__main__':
    manager.run()
