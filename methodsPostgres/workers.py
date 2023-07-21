import psycopg2
from flask import jsonify, make_response
from extensions.hashPassword import encoding
from extensions.connection import connect

def createTrabajador(nombre, telefono, direccion, puesto, id_trabajador, rol, password, user_app):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
        INSERT INTO trabajador (nombre, telefono, direccion, puesto, id_trabajador, rol, hash, user_app)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            ''', (nombre, telefono, direccion, puesto, id_trabajador, rol, encoding(password), user_app))
        cur.fetchall()
        
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])