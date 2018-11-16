# -*- coding: utf-8 -*-
__author__ = 'Eric Z. Eisberg'
__copyright__ = 'Copyright 2018 Eric Z. Eisberg'
__license__ = 'Licensed under MIT license'

import json
import os

import requests

SLACK_KEY = os.environ.get('SLACK_KEY') or None
SLACK_URL = 'https://slack.com/api/chat.postMessage'

def send_to_slack(email, blurb):
    if not SLACK_KEY:
        raise AttributeError('No slack key configured')
    bearer_key = 'Bearer %s' % SLACK_KEY
    headers = {'Content-Type': 'application/json', 'Authorization': bearer_key}
    body_text = 'Invitation request from %s.\n```%s```' % (email, blurb)
    data = {
        'as_user': False,
        'channel': 'admin',
        'text': body_text,
        'username': 'InviteBot',
    }
    response = requests.post(SLACK_URL, json=data, headers=headers)
    print(response.status_code)
