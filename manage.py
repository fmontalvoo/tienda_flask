from flask_script import Manager

from app import init_app

app = init_app()
app.config['DEBUG'] = True

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
