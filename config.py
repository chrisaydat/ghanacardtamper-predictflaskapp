import  os

from os import environ

class Config(object):

    Debug = False
    Testing = False


    basedor = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'my_secret_key'

    uploads = os.path.join(basedor, 'uploads')

    session_cookie_secure = True
    default_theme = None

    class DevelopmentConfig(Config):
        Debug = True
        session_cookie_secure = False

        class DebugConfig(Config):
            Debug = True
            session_cookie_secure = False