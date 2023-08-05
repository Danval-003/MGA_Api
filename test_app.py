import pytest
from app import app  # Importa tu aplicación Flask aquí
import json

# Prueba para el método makeLogin
def test_make_login():
    with app.test_client() as client:
        # Simula una solicitud POST a /login con datos de usuario y contraseña válidos
        data = {'password': '246810'}
        response = client.post('/login', json=data)

        # Verifica el código de respuesta y los datos devueltos
        assert response.status_code == 202
        resp_data = response.get_json()
        assert 'data' in resp_data
        assert 'error' in resp_data
        assert 'message' in resp_data
        assert 'session_token' in resp_data

        # Verifica los datos específicos devueltos
        assert resp_data['error'] == 202
        assert resp_data['message'] == 'Good Job'
        assert len(resp_data['data']) == 1
        assert 'direccion' in resp_data['data'][0]
        assert 'idTrabajador' in resp_data['data'][0]
        assert 'nombre' in resp_data['data'][0]
        assert 'puesto' in resp_data['data'][0]
        assert 'rol' in resp_data['data'][0]
        assert 'telefono' in resp_data['data'][0]



def test_obtain_login_user_token():
    with app.test_client() as client:
        # Simula una solicitud POST a /login con datos de usuario y contraseña válidos
        data = {'password': '246810'}
        response = client.post('/login', json=data)

        # Verifica el código de respuesta y los datos devueltos
        assert response.status_code == 202
        resp_data = response.get_json()
        assert 'data' in resp_data
        assert 'error' in resp_data
        assert 'message' in resp_data
        assert 'session_token' in resp_data

        # Verifica los datos específicos devueltos
        assert resp_data['error'] == 202
        assert resp_data['message'] == 'Good Job'
        assert len(resp_data['data']) == 1
        assert 'direccion' in resp_data['data'][0]
        assert 'idTrabajador' in resp_data['data'][0]
        assert 'nombre' in resp_data['data'][0]
        assert 'puesto' in resp_data['data'][0]
        assert 'rol' in resp_data['data'][0]
        assert 'telefono' in resp_data['data'][0]

        # Obtiene el session_token de la respuesta para usarlo en la siguiente solicitud
        session_token = resp_data['session_token']

        # Simula una solicitud GET a /getUser con el session_token en los encabezados
        headers = {'Authorization': f'Bearer {session_token}'}
        response = client.get('/getUser', headers=headers)

        # Verifica el código de respuesta y los datos devueltos
        assert response.status_code == 202
        resp_data = response.get_json()
        assert 'error' in resp_data
        assert 'message' in resp_data

        # Verifica los datos específicos devueltos
        assert resp_data['error'] == 202
        assert resp_data['nombre'] == 'Giovani Gonzalez'  # Asegúrate de ajustar este valor según tus datos
        assert resp_data['telefono'] == '45670934'  # Asegúrate de ajustar este valor según tus datos
        # Asegúrate de ajustar los demás campos según los datos devueltos por current_user.important_data()


def test_obtain_galerys():
    with app.test_client() as client:
        # Simula una solicitud POST a /login con datos de usuario y contraseña válidos
        data = {'password': '246810'}
        response = client.post('/login', json=data)

        # Verifica el código de respuesta y los datos devueltos para asegurarte de que el inicio de sesión sea exitoso
        assert response.status_code == 202
        resp_data = response.get_json()
        assert 'session_token' in resp_data

        # Obtiene el session_token de la respuesta para usarlo en la siguiente solicitud
        session_token = resp_data['session_token']

        # Simula una solicitud POST a /galeras con el session_token en los encabezados y datos JSON en el cuerpo
        data = {'numLote': 20}  # Asegúrate de proporcionar el dato necesario para la prueba
        headers = {'Authorization': f'Bearer {session_token}'}
        response = client.post('/galeras', json=data, headers=headers)

        # Verifica el código de respuesta y los datos devueltos
        assert response.status_code == 202
        resp_data = response.get_json()
        assert 'error' in resp_data
        assert 'message' in resp_data
        assert 'data' in resp_data

        # Verifica los datos específicos devueltos
        # Asegúrate de ajustar estos valores según lo que se espere en tu implementación
        assert resp_data['error'] == 202
        assert len(resp_data['data']) >= 1
        assert 'idGalera' in resp_data['data'][0]
        assert 'existence' in resp_data['data'][0]
        assert 'typeChicken' in resp_data['data'][0]
        assert 'numeroGalera' in resp_data['data'][0]
        assert 'ca' in resp_data['data'][0]
        assert 'idLote' in resp_data['data'][0]
