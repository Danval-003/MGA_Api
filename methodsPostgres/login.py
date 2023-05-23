from extensions.hashPassword import encoding
from extensions.connection import connect


def obtainUser(password, user):
    passEncoding = encoding(password)
    con = connect()
    cur = con.cursor()
    cur.execute()