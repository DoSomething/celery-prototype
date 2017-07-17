from flask import Blueprint

from .tasks import print_params

web = Blueprint('gambit', __name__)

@web.route('/')
def index():
    return 'Gambit'


@web.route('/mdata')
def mdata():
    # print(print_params)
    print_params.apply_async(args=[1])
    return 'Done', 201
