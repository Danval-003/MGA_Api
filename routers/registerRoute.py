from flask import Blueprint, request
from flask_login import login_user, current_user, login_required
from extensions.rol_identify import only_worker
from methodsPostgres.register import *

register_bp = Blueprint('register', __name__)


@register_bp.route('/makeRegister', methods=['POST'])
@only_worker
@login_required
def makeRegist():
    res = request.get_json()
    user = current_user.important_data()
    id_tr = str(user['idTrabajador'])
    parameters = ['cantidadAlimento', 'decesos', 'observaciones', 'idGalera', 'pesado']
    if 'cantidadAlimento' not in res or 'decesos' not in res or 'observaciones' not in res or 'idGalera' not in res \
            or 'pesado' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros num_galera y num_lote'}, 404))
    lista = []
    for i in parameters:
        lista.append(res[i])
    lista.append(id_tr)

    infoTupla = tuple(lista)

    return makeRegister(infoTupla)


@register_bp.route('/obtainRegistersDate', methods=['POST'])
def obtainRegisterDate():
    res = request.get_json()
    query = """select * from registers """

    if 'date' in res or 'idTrabajador' in res or 'idLote' in res:
        query = query + ' where'
        if 'date' in res:
            query = query + " fecha > '" + res['date'] + " 0:0:0.0' and  fecha < '" + res['date'] + " 23:59:59.0' and"
        if 'idTrabajador' in res:
            query = query + " id_trabajador = '%s' and" % (res['idTrabajador'],)
        if 'idLote' in res:
            query = query + " id_lote = %s and" % (res['idLote'],)
        print(query)
        query = query[:-3]

    return obtainRegisters(query)


@register_bp.route('/obtainTrabajadores', methods=['GET'])
def obtainTrabajador():
    return obtainTrabajadores()
