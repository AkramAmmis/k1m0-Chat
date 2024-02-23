from flask import Blueprint, render_template, abort, url_for, jsonify, session
from jinja2 import TemplateNotFound
from app.google_auth import google, oauth
import os
import json
auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login')
def login():
    redirect_uri = url_for('auth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    userinfo = resp.json()
    return 'hallo {}'.format(userinfo['name'])