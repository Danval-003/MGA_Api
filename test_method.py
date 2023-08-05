import pytest
from methodsPostgres.login import *
from methodsPostgres.galerys import *

# Prueba para el método do_login
def test_do_login():
    # Ejecuta el método do_login con datos de usuario y contraseña válidos
    user = 'admin'
    password = 'Admin'
    rol = 'admin'
    resp = do_login(user, password, rol)

    # Verifica la respuesta devuelta por do_login
    assert 'data' in resp
    assert 'error' in resp
    assert 'message' in resp

    # Verifica los datos específicos devueltos
    assert resp['error'] == 202
    assert resp['message'] == 'Good Job'
    assert len(resp['data']) == 1
    assert 'direccion' in resp['data'][0]
    assert 'idTrabajador' in resp['data'][0]
    assert 'nombre' in resp['data'][0]
    assert 'puesto' in resp['data'][0]
    assert 'rol' in resp['data'][0]
    assert 'telefono' in resp['data'][0]


def test_obtain_galery():
    # Ejecuta el método do_login con datos de usuario y contraseña válidos
    user = "20"
    password = "1"
    resp = obtainGaleras(user, password)

    # Verifica la respuesta devuelta por do_login
    assert 'data' in resp
    assert 'error' in resp
    assert 'message' in resp

    # Verifica los datos específicos devueltos
    assert resp['error'] == 202
    assert resp['message'] == 'Good Job'
    assert len(resp['data']) >= 1
    assert 'idGalera' in resp['data'][0]
    assert 'existence' in resp['data'][0]
    assert 'typeChicken' in resp['data'][0]
    assert 'numeroGalera' in resp['data'][0]
    assert 'ca' in resp['data'][0]
    assert 'idLote' in resp['data'][0]
