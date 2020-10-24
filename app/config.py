import os


class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    SECRET_KEY = os.urandom(32)
