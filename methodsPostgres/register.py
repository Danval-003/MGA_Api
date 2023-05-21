import psycopg2
from flask import jsonify, make_response

from extensions.connection import connect


def makeRegister(tupleValues):
    print(tupleValues)
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()  # Establish a connection to your database
        cur = conn.cursor()
        cur.execute('''
            SELECT * from register(%s, %s, %s, %s, %s)
            ''', tupleValues)
        conn.commit()
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])


def obtainRegisters(date):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()  # Establish a connection to your database
        cur = conn.cursor()
        cur.execute("""select cantidad_alimento, decesos, observaciones, fecha, ca, id_galera, id_registro, pesado
         from registro where fecha > '"+date+" 0:0:0.0' and  fecha < '"+date+" 23:59:59.0' """)
        rows = cur.fetchall()
        status['data'] = [
            {
                'cantidadAlimento': row[0],
                'decesos': row[1],
                'observaciones': row[2],
                'fecha': row[3],
                'ca': row[4],
                'idGalera': row[5],
                'idRegistro': row[6],
                'pesoMedido': row[7]

            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])
