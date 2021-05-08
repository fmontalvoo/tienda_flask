from flask import Flask, render_template

app = Flask(__name__)


# Paginas de la aplicacion
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('auth/login.html')

# Manejos de Errores


def page_not_found(error):
    return render_template('errors/404.html'), 404


def init_app(settings):
    app.config.from_object(settings)
    app.register_error_handler(404, page_not_found)
    return app
