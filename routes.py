# -*- coding: utf-8 -*-
__author__ = 'Eric Z. Eisberg'
__copyright__ = 'Copyright 2018 Eric Z. Eisberg'
__license__ = 'Licensed under MIT license'

import requests
from flask import render_template

from splashpage import app
from splashpage.forms import IntroForm
import splashpage.utils

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = IntroForm()
    if form.validate_on_submit():
        splashpage.utils.send_to_slack(form.email.data, form.blurb.data)
        return render_template('thanks.html')
    return render_template('index.html', title='EngiSciMath', form=form)
