from flask import Blueprint, request

from methodsPostgres.login import *

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST'])
def obtainLotes():
    res = request.get_json()
    if 'password' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros user y password'}, 404))
    rol = 'trabajador'
    user = ''
    if 'user' in res:
        user = res['user']
        rol = 'admin'

    return do_login(user, res['password'], rol)
