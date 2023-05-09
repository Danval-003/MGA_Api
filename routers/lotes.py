from flask import Blueprint, request

from methodsPostgres.lotes import *

lotes_bp = Blueprint('lotes', __name__)


@lotes_bp.route('/lObtain', methods=['POST'])
def obtainLotes():
    res = request.get_json()
    if 'dpiTrabajador' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros dpiTrabajador'}, 404))

    infoTupla = tuple([res['dpiTrabajador']])

    return obtainLote(infoTupla)