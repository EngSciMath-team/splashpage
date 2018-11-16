# -*- coding: utf-8 -*-
__author__ = 'Eric Z. Eisberg'
__copyright__ = 'Copyright 2018 Eric Z. Eisberg'
__license__ = 'Licensed under MIT license'

from flask import Flask
from splashpage.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from splashpage import routes
