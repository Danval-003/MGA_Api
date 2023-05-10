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
