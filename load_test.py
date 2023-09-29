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

    # Agrega más tareas de prueba según sea necesario
