class Settings:
    SECRET_KEY = 'B!.23W#$ERT^&SDFG'


class DelelopmentSettings(Settings):
    DEBUG = True


settings = {
    'development': DelelopmentSettings,
    'default': DelelopmentSettings
}
