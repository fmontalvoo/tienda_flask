from werkzeug.security import generate_password_hash, check_password_hash


class Usuario():

    def __init__(self, id, usuario, password, tipo_usuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo_usuario = tipo_usuario

    def crypt_password(self, password):
        crypt = generate_password_hash(password)
        checked = check_password_hash(crypt, password)
        return checked
