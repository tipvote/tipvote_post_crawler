# coding=utf-8
from passwords import \
    database_connection, \
    mailuser, \
    mailpass, \
    secretkey, \
    wtfkey

SQLALCHEMY_DATABASE_URI_0 = database_connection

SQLALCHEMY_BINDS = {
    'avengers': SQLALCHEMY_DATABASE_URI_0,
}

SQLALCHEMY_TRACK_MODIFICATIONS = False