import psycopg2


# Funcion que realiza la coneccion a la base de datos
def connect(user='postgres', password='123456'):
    # Se le manda la informacion para realizar la coneccion
    conn = psycopg2.connect(
        host="localhost",
        database="galeryDataBase",
        user=user,
        password=password
    )
    return conn