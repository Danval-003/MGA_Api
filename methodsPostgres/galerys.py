import psycopg2
from flask import jsonify, make_response
from extensions.connection import connect


def obtainGaleras(info_lote, id_tr):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
        select * from get_galeries('''+info_lote+""",'"""+id_tr+"""');
            """, )
        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[5],
                'typeChicken': row[3],
                'numeroGalera': row[1],
                'ca': row[4]
            }
            for row in rows
        ]
        status['message'] = 'Good Job' if len(status['data']) > 0 else 'Esta vacia'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return status


def obtainGalerasZ(id_tr):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
        select * from get_galeriesW('"""+id_tr+"""');
            """, )

        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[5],
                'typeChicken': row[3],
                'numeroGalera': row[1],
                'idLote': row[2],
                'ca': row[4],
                'fechaInicio': row[5]
            }
            for row in rows
        ]
        status['message'] = 'Good Job' if len(status['data']) > 0 else 'Esta vacia'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return status


def obtainGalerasAdm(idLot):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
        select * from get_galeriesadm(%s);
            """, (int(idLot),))

        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[5],
                'typeChicken': row[3],
                'numeroGalera': row[1],
                'idLote': row[2],
                'ca': row[4]
            }
            for row in rows
        ]
        status['message'] = 'Good Job' if len(status['data']) > 0 else 'Esta vacia'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return status


def infoGalera(tupleValues):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
                Select id_galera, gi.exitencia, tipo_pollo, EXTRACT(days FROM age(CURRENT_DATE::timestamp with time zone, fecha_inicio::timestamp with time zone)) AS edad
                from galeras g inner join galeras_info gi on g.id_galera = gi.id_galera where id_lote = %s and numero = %s;
            ''', tupleValues)
        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[1],
                'typeChicken': row[2],
                'edad': row[3]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])

def createGaleras(id_galera, id_lote, no_galera, existencia, tipo_pollo, id_trabajador, fecha_inicio):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
        select * from nueva_galera(%s, %s, %s, %s, %s, %s, %s)
            ''', (id_galera, id_lote, no_galera, existencia, tipo_pollo, id_trabajador, fecha_inicio))
        cur.fetchall()
        conn.commit()
        
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])
