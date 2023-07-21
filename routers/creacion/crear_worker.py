from flask import Blueprint, request
from methodsPostgres.workers import *

worker_bp = Blueprint('worker', __name__)

@worker_bp.route('/wcreate', methods=['POST'])
def createW():
    res = request.get_json()
    if 'nombre' not in res or 'telefono' not in res or 'direccion' not in res or 'puesto' not in res or 'id_trabajador' not in res or 'rol' not in res or 'password' not in res or 'user_app' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros para la creacion del nuevo trabajador'}, 404))

    return createTrabajador(res['nombre'], res['telefono'], res['direccion'], res['puesto'], res['id_trabajador'], res['rol'], res['password'], res['user_app'])

#nombre, telefono, direccion, puesto, id_trabajador, rol, password, user_app