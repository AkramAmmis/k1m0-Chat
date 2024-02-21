from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def index():
    try:
        return render_template('index.html', title='Home', css_file='home.css')
    except TemplateNotFound:
        print('TemplateNotFound')
        abort(404)