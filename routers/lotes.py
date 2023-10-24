from flask import Blueprint, request
from flask_login import login_user, current_user, login_required
from extensions.rol_identify import only_worker
from extensions.cache import cache

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


@lotes_bp.route('/loteObtain', methods=['GET'])
@only_worker
@login_required
@cache.cached(timeout=60)
def obtainLotesForWorked():
    user = current_user.important_data()
    id_tr = str(user['idTrabajador'])
    infoTupla = tuple([id_tr])

    return obtainLote(infoTupla)
