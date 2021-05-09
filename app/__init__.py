from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user

from .models.entities.usuario import Usuario

from .models.libro_dao import LibroDao
from .models.usuario_dao import UsuarioDao


# CSRF (Cross-site Request Forgery): Solicitud de falsificacion entre sitios.
csrf = CSRFProtect()

app = Flask(__name__)

db = MySQL(app)

login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return UsuarioDao.obtener_por_id(db, id)


# Rutas de la aplicacion
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['user'], request.form['password'], None)
        logged_user = UsuarioDao.login(db, usuario)
        if logged_user != None:
            login_user(logged_user)
            return redirect(url_for('index'))
        else:
            flash("Usuario o contraseña incorrectos")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash("Terminaste la sesión")
    return redirect(url_for('login'))


@app.route('/libros')
def listar_libros():
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
