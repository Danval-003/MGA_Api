from flask import Blueprint, request
from methodsPostgres.workers import *

worker_bp = Blueprint('worker', __name__)

@galery_bp.route('/gcreate', methods=['POST'])
def createG():
    res = request.get_json()
    if 'numGalera' not in res or 'numLote' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros num_galera y num_lote'}, 404))

    infoTupla = tuple([res['numLote'], res['numGalera']])