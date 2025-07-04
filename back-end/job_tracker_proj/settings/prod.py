from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "3.145.156.111",
    "0.0.0.0"
]


CORS_ALLOWED_ORIGINS = [
    "http://3.145.156.111",
]

CSRF_TRUSTED_ORIGINS = [
    "http://3.145.156.111",
]

SECURE_SSL_REDIRECT     = True
SESSION_COOKIE_SECURE   = True
CSRF_COOKIE_SECURE      = True
