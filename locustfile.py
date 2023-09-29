from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Tiempo de espera entre solicitudes

    @task
    def test_login(self):
        data = {'password': 'Admin', 'user': 'admin'}
        self.client.post('/login', json=data)

    @task
    def test_make_login(self):
        data = {'password': '246810'}
        self.client.post('/login', json=data)

    @task
    def test_obtain_login_user_token(self):
        data = {'password': '246810'}
        response = self.client.post('/login', json=data)
        session_token = response.json().get('session_token', '')
        headers = {'Authorization': f'Bearer {session_token}'}
        self.client.get('/getUser', headers=headers)

    @task
    def test_obtain_galerys(self):
        data = {'password': '246810'}
        response = self.client.post('/login', json=data)
        session_token = response.json().get('session_token', '')
        headers = {'Authorization': f'Bearer {session_token}'}
        self.client.get('/galerasWorker', headers=headers)

    @task
    def test_make_register(self):
        data = {'password': '246810'}
        response = self.client.post('/login', json=data)
        session_token = response.json().get('session_token', '')
        headers = {'Authorization': f'Bearer {session_token}'}
        info = {'cantidadAlimento': 0, 'decesos': 0, 'observaciones': '0', 'idGalera': '0000PD', 'pesado': 200}
        self.client.post('/makeRegister', json=info, headers=headers)

    @task
    def test_obtain_lotes(self):
        data = {'password': '246810'}
        response = self.client.post('/login', json=data)
        session_token = response.json().get('session_token', '')
        headers = {'Authorization': f'Bearer {session_token}'}
        self.client.get('/loteObtain', headers=headers)

    @task
    def test_obtain_registers(self):
        data = {'password': '246810'}
        response = self.client.post('/login', json=data)
        session_token = response.json().get('session_token', '')
        headers = {'Authorization': f'Bearer {session_token}'}
        data = {"date": "2023-09-22", "idLote": "2"}
        self.client.post('/obtainRegistersDate', json=data, headers=headers)
