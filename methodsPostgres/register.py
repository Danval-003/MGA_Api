import psycopg2
from flask import jsonify, make_response

from extensions.connection import connect


def makeRegister(tupleValues):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()  # Establecer una conexión a tu base de datos
        cur = conn.cursor()

        # Intentar adquirir un bloqueo de fila exclusivo en la tabla galeras_info
        # para la galera específica antes de llamar a la función register
        cur.execute("SELECT 1 FROM galeras_info WHERE id_galera = %s FOR UPDATE NOWAIT", (tupleValues[3],))

        # Llamar a la función register dentro de la transacción
        cur.execute('SELECT * FROM register(%s, %s, %s, %s, %s, %s)', tupleValues)

        # Realizar COMMIT ya que hemos adquirido el bloqueo
        conn.commit()

        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        # Manejar excepciones
        conn.rollback()  # Realizar rollback en caso de error
        status['message'] = str(e)
        status['error'] = 404
    finally:
        conn.close()

    return make_response(jsonify(status), status['error'])


def obtainRegisters(query):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()  # Establish a connection to your database
        cur = conn.cursor()
        cur.execute(query)
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
                'pesoMedido': row[7],
                'edadGalera': row[8],
                'tipoPollo': row[9]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])


def obtainTrabajadores():
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()  # Establish a connection to your database
        cur = conn.cursor()
        cur.execute('select nombre, telefono, direccion, puesto, id_trabajador, url_image from trabajador;')
        rows = cur.fetchall()
        status['data'] = [
            {
                'nombre': row[0],
                'telefono': row[1],
                'direccion': row[2],
                'puesto': row[3],
                'idTrabajador': row[4],
                'img': row[5] if row[5] is not None else 'N.A'
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])
