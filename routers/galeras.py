from flask import Blueprint, request
from flask_login import login_user, current_user, login_required
from extensions.rol_identify import only_worker
from methodsPostgres.galerys import *

galery_bp = Blueprint('galery', __name__)


@galery_bp.route('/gObtain', methods=['POST'])
def obtainG():
    res = request.get_json()
    if 'numGalera' not in res or 'numLote' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros num_galera y num_lote'}, 404))

    infoTupla = tuple([res['numLote'], res['numGalera']])

    return infoGalera(infoTupla)


@galery_bp.route('/galeras', methods=['POST'])
@only_worker
@login_required
def obtainGaleriars():
    res = request.get_json()
    user = current_user.important_data()
    id_tr = str(user['idTrabajador'])
    if 'numLote' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros num_lote'}, 404))
    resp = current_user.important_data()
    infoLote = str(res['numLote'])
    status = obtainGaleras(infoLote, id_tr)

    return make_response(jsonify(status), status['error'])
