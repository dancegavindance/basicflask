from flask import Blueprint

numpy = Blueprint('numpy', __name__, url_prefix = '/numpy')

@numpy.route('/')
@numpy.route('/index')
def index():
    return "numpy"
