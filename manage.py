import os
import unittest

from flask_migrate import Migrate
from flask_script import Manager

from app.main import create_app, db
from app.main.model import user
from app import blueprint

app = create_app(os.getenv('APP_ENV', 'dev'))
app.register_blueprint(blueprint)

app.app_context().push()

@app.before_first_request
def create_tables():
    db.create_all()

manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def run():
    app.run()

@manager.command
def test():
    tests = unittest.TestLoader().discover('app/tests', pattern="*.test.py")
    results = unittest.TextTestRunner(verbosity=2).run(tests)

    if results.wasSuccessful():
        return 0
    return 1 

if __name__ == '__main__':
    manager.run()