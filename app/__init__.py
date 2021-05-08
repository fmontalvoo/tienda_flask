from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Paginas de la aplicacion
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if(request.form['user'] == 'admin' and request.form['password'] == '123'):
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# Manejos de Errores


def page_not_found(error):
    return render_template('errors/404.html'), 404


def init_app(settings):
    app.config.from_object(settings)
    app.register_error_handler(404, page_not_found)
    return app
