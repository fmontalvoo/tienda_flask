from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from .models.entities.usuario import Usuario

from .models.libro_dao import LibroDao
from .models.usuario_dao import UsuarioDao


# CSRF (Cross-site Request Forgery): Solicitud de falsificacion entre sitios.
csrf = CSRFProtect()

app = Flask(__name__)

db = MySQL(app)


# Paginas de la aplicacion
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['user'], request.form['password'], None)
        auth = UsuarioDao.login(db, usuario)
        if auth != None:
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/libros')
def libros():
    try:
        libros = LibroDao.listar_libros(db)
        data = {'libros': libros}
        return render_template('lista_libros.html', data=data)
    except Exception as ex:
        print(ex)


# Manejos de Errores
def page_not_found(error):
    return render_template('errors/404.html'), 404


def init_app(settings):
    app.config.from_object(settings)
    csrf.init_app(app)
    app.register_error_handler(404, page_not_found)
    return app
