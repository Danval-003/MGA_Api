from flask import Blueprint, request, jsonify, make_response
from extensions.User_object import User
from methodsPostgres.login import *
from flask_login import login_user, current_user, login_required
from extensions.cryptografic import encrypth
from extensions.rol_identify import only_worker, only_admin

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST'])
def makeLogin():
    res = request.get_json()
    if 'password' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros user y password'}, 404))
    rol = 'trabajador'
    user = ''
    if 'user' in res:
        user = res['user']
        rol = 'admin'
    else:
        res['user'] = None

    resp = do_login(user, res['password'], rol)

    if resp['error'] == 202:
        id_us = encrypth({'user': res['user'], 'password': res['password'], 'rol': rol})
        user = User(id_us)
        login_user(user, remember=True)
        resp.update({'session_token': id_us})

    return make_response(jsonify(resp), resp['error'])


@login_bp.route('/getUser', methods=['GET'])
@login_required
def getUser():
    if current_user.is_authenticated:
        resp = current_user.important_data()
        return make_response(jsonify(resp), 202)
    else:
        return make_response(jsonify({'message': 'Usuario no autenticado'}), 401)


@login_bp.route('/getWorker', methods=['GET'])
@only_worker
@login_required
def getWorker():
    return make_response(jsonify({'error': 'exito'}), 202)


@login_bp.route('/getAdmin', methods=['GET'])
@only_admin
@login_required
def getAdmin():
    return make_response(jsonify({'error': 'exito'}), 202)
