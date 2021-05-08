class Settings:
    pass


class DelelopmentSettings(Settings):
    DEBUG = True


settings = {
    'development': DelelopmentSettings,
    'default': DelelopmentSettings
}
