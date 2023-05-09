from flask import Blueprint, request
from methodsPostgres.galerys import *

galery_bp = Blueprint('galery', __name__)


@galery_bp.route('/gObtain', methods=['GET'])
def obtainG():
    res = request.get_json()
    if 'numGalera' not in res or 'numLote' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros num_galera y num_lote'}, 404))

    infoTupla = tuple([res['numLote'], res['numGalera']])

    return infoGalera(infoTupla)


@galery_bp.route('/galeras', methods=['GET'])
def obtainGaleriars():
    res = request.get_json()
    if 'numLote' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros num_lote'}, 404))

    infoTupla = res['numLote']

    return obtainGaleras(infoTupla)
