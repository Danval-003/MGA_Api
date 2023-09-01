import psycopg2
from flask import jsonify, make_response
from extensions.connection import connect

def wxLote(id_lote):
    status = {
        'error': 202,
        'message': '',
        'data': []
    }
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
        select trabajador.nombre, trabajador.id_trabajador 
        from (galeras_info inner join trabajador on galeras_info.id_trabajador = trabajador.id_trabajador)
            inner join galeras on galeras_info.id_galera = galeras.id_galera
        where galeras.id_lote = %s
        group by trabajador.id_trabajador;
            ''', id_lote)
        rows = cur.fetchall()

        status['data'] = [
            {
                'nombre_trabajador': row[0],
                'id_trabajador': row[1]
            }
            for row in rows
        ]
        status['message'] = 'Good Job'
    except psycopg2.Error as e:
        status['message'] = str(e)
        status['error'] = 404

    return make_response(jsonify(status), status['error'])