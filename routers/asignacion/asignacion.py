from flask import Blueprint, request
from methodsPostgres.asignation import *

asignation_bp = Blueprint('asignation', __name__)

@asignation_bp.route('/asignate', methods=['POST'])
def asignateGW():
    res = request.get_json()
    if 'new_id_lote' not in res or 'new_no_galera' not in res or 'new_id_trabajador' not in res or 'new_fecha_inicio' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros para una nueva asignacion'}, 404))

    return Asignation(res['new_id_lote'], res['new_no_galera'], res['new_id_trabajador'], res['new_fecha_inicio'])

#new_id_lote, new_no_galera, new_id_trabajador, new_fecha_inicio