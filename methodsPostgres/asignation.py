import psycopg2
from flask import jsonify, make_response
from extensions.connection import connect

def Asignation(new_id_galera, old_id_galera, new_id_trabajador, new_fecha_inicio):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
        select * asignar_galeras(%s, %s, %s, %s);
            ''', (new_id_galera, old_id_galera, new_id_trabajador, new_fecha_inicio))
        cur.fetchall()
        
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])