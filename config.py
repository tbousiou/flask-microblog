import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER =  'smtp.mailtrap.io'
    MAIL_PORT = 25
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'ef9cd3b392bece'
    MAIL_PASSWORD = 'a802660defa5a0'
    ADMINS = ['tbousiou@gmail.com']
