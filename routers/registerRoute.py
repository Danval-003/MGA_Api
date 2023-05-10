from flask import Blueprint, request
from methodsPostgres.register import *

register_bp = Blueprint('register', __name__)


@register_bp.route('/makeRegister', methods=['POST'])
def makeRegister():
    res = request.get_json()
    parameters = ['cantidadAlimento', 'decesos', 'observaciones', 'idGalera', 'pesado']
    if 'cantidadAlimento' not in res or 'decesos' not in res or 'observaciones' not in res or 'idGalera' not in res or 'pesado' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros num_galera y num_lote'}, 404))
    lista = []
    for i in parameters:
        lista.append(res[i])

    infoTupla = tuple(lista)

    return makeRegister(infoTupla)
