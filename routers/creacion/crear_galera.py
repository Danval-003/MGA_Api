from flask import Blueprint, request
from methodsPostgres.galerys import *
from datetime import date, datetime
import pytz

cgalery_bp = Blueprint('cgalery', __name__)


@cgalery_bp.route('/gcreate', methods=['POST'])
def createG():
    res = request.get_json()
    if 'id_lote' not in res or 'no_galera' not in res or 'existencia' not in res or 'tipo_pollo' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros para la creacion de la nueva galera'},
            404))

    zona_horaria_guatemala = pytz.timezone('America/Guatemala')
    today = datetime.now(zona_horaria_guatemala).date()
    res['id_galera'] = res['id_lote'] + res['no_galera'] + str(today)

    data = tuple(res['id_lote'], res['no_galera'], res['existencia'], res['tipo_pollo'], res['id_galera'])

    return createGalery(data)


# id_galera, id_lote, no_galera, existencia, tipo_pollo, id_trabajador, fecha_inicio
