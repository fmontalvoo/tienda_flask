from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin):

    def __init__(self, id, usuario, clave, tipo_usuario):
        self.id = id
        self.usuario = usuario
        self.clave = clave
        self.tipo_usuario = tipo_usuario

    def crypt_password(self, password):
        crypt = generate_password_hash(password)
        checked = check_password_hash(crypt, password)
        return checked

    @classmethod
    def check_password(self, user_password, password):
        return check_password_hash(user_password, password)
