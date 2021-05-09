from decouple import config


class Settings:
    SECRET_KEY = 'B!.23W#$ERT^&SDFG'


class DelelopmentSettings(Settings):
    DEBUG = True
    MYSQL_HOST = '192.168.1.38'
    MYSQL_USER = 'admin'
    MYSQL_PASSWORD = 'Admin.123'
    MYSQL_DB = 'tienda_db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_PASSWORD = config('MAIL_PASSWORD')


settings = {
    'development': DelelopmentSettings,
    'default': DelelopmentSettings
}
