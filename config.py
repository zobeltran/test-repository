"""
This is the Configuration
"""


class BaseConfig(object):
    """ This is the main config class to be inherited """
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """ This is the main configuration class """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\Renzo\Documents\Codes\Python\isproj2-fcth-crm\dev\crm.db'
    SECRET_KEY = 'developmentsecretkey'
    UPLOAD_FOLDER = 'app/upload'
    # Flask User Configurations
    USER_ENABLE_EMAIL = True 
    USER_AFTER_CHANGE_PASSWORD_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_CHANGE_USERNAME_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_CONFIRM_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_FORGOT_PASSWORD_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_LOGIN_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_LOGOUT_ENDPOINT = 'user.login'    # v0.5.3 and up
    USER_AFTER_REGISTER_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_RESEND_CONFIRM_EMAIL_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_RESET_PASSWORD_ENDPOINT = 'main.homepage'              # v0.6 and up
    USER_INVITE_ENDPOINT = 'main.homepage'              # v0.6.2 and up
    # Flask Mail Configurations
    MAIL_SERVER = 'mail.ideafy-it.com'
    MAIL_PORT = 26
    MAIL_USE_SSL = False 
    MAIL_USE_TSL = False
    MAIL_USERNAME = 'renzobeltran@ideafy-it.com'
    MAIL_PASSWORD = 'P@55w0rd1'
    MAIL_DEFAULT_SENDER = 'renzobeltran@ideafy-it.com'
    RECAPTCHA_PUBLIC_KEY = '6LckujcUAAAAAERy3iVKuP-hxkYH7p9LeISLYuf5'
    RECAPTCHA_PRIVATE_KEY = '6LckujcUAAAAAPbJc_U5wLXLPvY7xzKuDQui_jrW'


class ProductionConfig(BaseConfig):
    """ This is the production configuration class """
    DATABASE = ''.join(['postgresql://zccisfiglvdagd:',
                        '5d5fe904f02e350ca33066c2a51a5c6cc0c5236ade95b403cea2418d0ca567c2',
                        '@ec2-54-243-255-57.compute-1.amazonaws.com:5432/dfn8ta0mogh2u9'])
    SECRET_KEY = '\xd6;\x9aq)\xea\xa5\x9c\xf5BM^N\x05X\\\xec5w\x0f\xb9\xab\xf9\xb8'
    UPLOAD_FOLDER = 'app/upload'
    SQLALCHEMY_DATABASE_URI = DATABASE
    USER_ENABLE_EMAIL = True
    USER_APP_NAME = 'CRM-FCTH' 
    USER_AFTER_CHANGE_PASSWORD_ENDPOINT = 'user.profile'              # v0.5.3 and up
    USER_AFTER_CHANGE_USERNAME_ENDPOINT = 'user.profile'              # v0.5.3 and up
    USER_AFTER_CONFIRM_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_FORGOT_PASSWORD_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_LOGIN_ENDPOINT = 'user.profile'              # v0.5.3 and up
    USER_AFTER_LOGOUT_ENDPOINT = 'user.login'    # v0.5.3 and up
    USER_AFTER_REGISTER_ENDPOINT = 'user.profile'              # v0.5.3 and up
    USER_AFTER_RESEND_CONFIRM_EMAIL_ENDPOINT = 'main.homepage'              # v0.5.3 and up
    USER_AFTER_RESET_PASSWORD_ENDPOINT = 'main.homepage'              # v0.6 and up
    USER_INVITE_ENDPOINT = 'main.homepage'
    # Flask Mail Configurations
    MAIL_SERVER = 'mail.ideafy-it.com'
    MAIL_PORT = 26
    MAIL_USE_SSL = False
    MAIL_USE_TSL = False
    MAIL_USERNAME = 'renzobeltran@ideafy-it.com'
    MAIL_PASSWORD = 'P@55w0rd1'
    MAIL_DEFAULT_SENDER = 'renzobeltran@ideafy-it.com'
    RECAPTCHA_PUBLIC_KEY = '6LckujcUAAAAAERy3iVKuP-hxkYH7p9LeISLYuf5'
    RECAPTCHA_PRIVATE_KEY = '6LckujcUAAAAAPbJc_U5wLXLPvY7xzKuDQui_jrW'
