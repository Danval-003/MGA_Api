from flask import Blueprint, request
from methodsPostgres.galerys import *

cgalery_bp = Blueprint('cgalery', __name__)

@cgalery_bp.route('/gcreate', methods=['POST'])
def createG():
    res = request.get_json()
    if 'id_galera' not in res or 'id_lote' not in res or 'no_galera' not in res or 'existencia' not in res or 'tipo_pollo' not in res or 'id_trabajador' not in res or 'fecha_inicio' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros para la creacion de la nueva galera'}, 404))
    
    return createGaleras(res['id_galera'], res['id_lote'], res['no_galera'], res['existencia'], res['tipo_pollo'], res['id_trabajador'], res['fecha_inicio'])
    
#id_galera, id_lote, no_galera, existencia, tipo_pollo, id_trabajador, fecha_inicio