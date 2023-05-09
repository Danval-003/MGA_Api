import psycopg2
from flask import jsonify, make_response

from extensions.connection import connect


def obtainGaleras(tupleValues):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
            Select id_galera, existencia, tipo_pollo, id_trabajador from galera where id_lote = %s;
            ''', tupleValues)
        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[1],
                'typeChicken': row[2],
                'idWorker': row[3]
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
            Select id_galera, existencia, tipo_pollo, id_trabajador from galera where id_lote = %s and numero = %s;
            ''', tupleValues)
        rows = cur.fetchall()

        status['data'] = [
            {
                'idGalera': row[0],
                'existence': row[1],
                'typeChicken': row[2],
                'idWorker': row[3]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])
