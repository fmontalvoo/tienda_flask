from .entities.usuario import Usuario
from .entities.tipo_usuario import TipoUsuario


class UsuarioDao():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, usuario, password 
                    FROM usuario WHERE usuario = '{0}'""".format(usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                coincide = Usuario.verificar_password(
                    data[2], usuario.password)
                if coincide:
                    usuario_logeado = Usuario(data[0], data[1], None, None)
                    return usuario_logeado
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT USU.id, USU.usuario, TIP.id, TIP.nombre 
                    FROM usuario USU JOIN tipo_usuario TIP ON USU.tipo_usuario_id = TIP.id 
                    WHERE USU.id = {0}""".format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            tipo_usuario = tipo_usuario(data[2], data[3])
            usuario_logeado = Usuario(data[0], data[1], None, tipo_usuario)
            return usuario_logeado
        except Exception as ex:
            raise Exception(ex)
