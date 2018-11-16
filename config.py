import os

class Config(object):
    SECRET_KEY = os.environ.get('CQRS') or 'STOCK-CQRS-KEY'
