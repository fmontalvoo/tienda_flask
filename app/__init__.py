from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from .models.entities.usuario import Usuario

from .models.libro_dao import LibroDao
from .models.usuario_dao import UsuarioDao

from .consts import *


# CSRF (Cross-site Request Forgery): Solicitud de falsificacion entre sitios.
csrf = CSRFProtect()

app = Flask(__name__)

db = MySQL(app)

login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    """
    Carga al usuario en la sesion actual.
    """
    return UsuarioDao.obtener_por_id(db, id)


# Rutas de la aplicacion
@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipo_usuario.id == 1:
            libros_vendidos = []
            data = {"titulo": "Libros Vendidos",
                    "libros_vendidos": libros_vendidos}
        else:
            compras = []
            data = {"titulo": "Mis compras",
                    "compras": compras}
        return render_template('index.html', data=data)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['user'], request.form['password'], None)
        logged_user = UsuarioDao.login(db, usuario)
        if logged_user != None:
            login_user(logged_user)
            flash(WELCOME_MESSAGE, 'success')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_FAILURE, 'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@app.route('/libros')
@login_required
def listar_libros():
    try:
        libros = LibroDao.listar_libros(db)
        data = {'libros': libros}
        return render_template('lista_libros.html', data=data)
    except Exception as ex:
        return render_template('errors/error.html', mensaje=format(ex))


# Manejos de Errores
def page_not_found(error):
    return render_template('errors/404.html')


def unauthorized_access(error):
    return redirect(url_for('login'))


def init_app(settings):
    app.config.from_object(settings)
    csrf.init_app(app)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, unauthorized_access)
    return app
