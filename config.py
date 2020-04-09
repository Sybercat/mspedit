class Configuration(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://main_user:main_pass@localhost:5432/main_mosprom'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sdkjfskdjfbekj'
    SECURITY_PASSWORD_SALT = 'w,mndk.jbeWK'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
