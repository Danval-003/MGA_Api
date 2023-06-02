import psycopg2
from flask import make_response, jsonify

from extensions.connection import connect


def obtainLote(tupleValues):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''select id_lote from lote where id_trabajador = %s; ''', tupleValues)
        rows = cur.fetchall()

        status['data'] = [
            {
                'idLote': row[0]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])
