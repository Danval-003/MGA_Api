import psycopg2
from flask import jsonify, make_response

from extensions.hashPassword import encoding
from extensions.connection import connect


def do_login(user, password, rol):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        passEncoding = encoding(password)
        con = connect()
        cur = con.cursor()
        cur.execute('select * from do_login(%s, %s, %s)', (user, str(passEncoding), rol))
        rows = cur.fetchall()

        status['data'] = [
            {
                'nombre': row[0],
                'telefono': row[1],
                'direccion': row[2],
                'puesto': row[3],
                'idTrabajador': row[4],
                'rol': row[5]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])