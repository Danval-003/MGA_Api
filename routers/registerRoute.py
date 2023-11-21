from flask import Blueprint, request
from flask_login import login_user, current_user, login_required
from extensions.rol_identify import only_worker
from methodsPostgres.register import *
from extensions.cache import cache
from extensions.smsAlert import enviar_sms

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
    if res['desesos'] >=5:
        enviar_sms(str(current_user.get_name_u()),res['desesos'])

    for i in parameters:
        lista.append(res[i])
    lista.append(id_tr)

    infoTupla = tuple(lista)
    print(infoTupla)

    return makeRegister(infoTupla)


@register_bp.route('/obtainRegistersDate', methods=['POST'])
def obtainRegisterDate():
    res = request.get_json()

    query = """select cantidad_alimento, decesos, observaciones, fecha, ca, g.id_galera, id_registro, pesado, date_part('day', g.fecha_inicio) - date_part('day', fecha), tipo_pollo from 
    registro inner join galeras g on g.id_galera = registro.id_galera 
    inner join galeras_info gi on registro.id_galera = gi.id_galera"""

    if 'date' in res or 'idTrabajador' in res or 'idLote' in res:
        query = query + ' where'
        if 'date' in res:
            query = query + " DATE(fecha) = '" + res['date'] + "' and"
        if 'idTrabajador' in res:
            query = query + " g.id_trabajador = '%s' and" % (res['idTrabajador'],)
        if 'idLote' in res:
            query = query + " id_lote = %s and" % (res['idLote'],)
        query = query[:-3]

    return obtainRegisters(query)


@register_bp.route('/obtainTrabajadores', methods=['GET'])
def obtainTrabajador():
    return obtainTrabajadores()


@register_bp.route('/obtainRanking', methods=['GET'])
def obtainRank():
    return obtainRanking()


@register_bp.route('/obtainInfoEnsayo', methods=['POST'])
def obtainInfEnsa():
    res = request.get_json()
    if 'id_gale' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros id_gale'}, 404))

    idg = res['id_gale']
    return obtainInfoEnsayo(str(idg))


@register_bp.route('/finishGale', methods=['POST'])
def finishS():
    res = request.get_json()
    if 'id_gale' not in res:
        return make_response(jsonify(
            {'message': 'Error al colocar los datos debias mandar como parametros id_gale'}, 404))

    idg = res['id_gale']
    return finished(str(idg))

