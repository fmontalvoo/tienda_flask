class Settings:
    SECRET_KEY = 'B!.23W#$ERT^&SDFG'


class DelelopmentSettings(Settings):
    DEBUG = True
    MYSQL_HOST = '192.168.1.38'
    MYSQL_USER = 'admin'
    MYSQL_PASSWORD = 'Admin.123'
    MYSQL_DB = 'tienda_db'


settings = {
    'development': DelelopmentSettings,
    'default': DelelopmentSettings
}
