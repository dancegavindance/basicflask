from flask import Blueprint

funky = Blueprint('funky', __name__, url_prefix = '/funky')

@funky.route('/')
@funky.route('/index')
def index():
    return "funky"


