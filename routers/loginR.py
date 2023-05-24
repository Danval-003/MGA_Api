from flask import Blueprint, request

from methodsPostgres.login import *

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST'])
def obtainLotes():
    res = request.get_json()
    if 'user' not in res and 'password' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros user y password'}, 404))

    return do_login(res['user'], res['password'])