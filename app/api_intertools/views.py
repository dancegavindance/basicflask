from flask import Blueprint

intertools = Blueprint('intertools', __name__, url_prefix = '/intertools')

@intertools.route('/')
@intertools.route('/index')
def index():
    return "intertools"