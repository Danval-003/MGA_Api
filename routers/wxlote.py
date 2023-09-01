from flask import Blueprint, request
from methodsPostgres.wxlote import *

wxlote_bp = Blueprint('wxlote', __name__)


@wxlote_bp.route('/wperLote', methods=['POST'])
def obtainWorkersxLote():
    res = request.get_json()
    if 'id_lote' not in res:
        return make_response(jsonify(
            {'message': 'Ingreso incorrecto de lote'}, 404))

    infoTupla = tuple([res['id_lote']])

    return wxLote(infoTupla)