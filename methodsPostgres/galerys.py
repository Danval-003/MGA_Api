import psycopg2
from flask import jsonify, make_response

from extensions.connection import connect


def obtainGaleras(id_lote):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
                select g.id_galera, numero, id_lote, tipo_pollo, ca, existencia
                from galera g
                left outer join registro r on g.id_galera = r.id_galera
                where id_lote = %s
                order by fecha desc;
            ''', (id_lote,))
        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[5],
                'typeChicken': row[3],
                'numeroGalera': row[1],
                'ca': row[4],
                'idLote': row[5]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])


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
            Select id_galera, existencia, tipo_pollo from galera where id_lote = %s and numero = %s;
            ''', tupleValues)
        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[1],
                'typeChicken': row[2]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])
