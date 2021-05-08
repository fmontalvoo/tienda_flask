from flask_script import Manager, Server

from app import init_app
from settings import settings

settings = settings['development']

app = init_app(settings)

manager = Manager(app)
manager.add_command('runserver', Server(host='localhost', port=3000))

if __name__ == '__main__':
    manager.run()
