from flask_login import UserMixin
from extensions.cryptografic import desencrypth
from methodsPostgres.login import do_login

dict_role = {
    'Admin': ['admin', 'El mejor jefe del mundo'],
    'Medico': ['medico', 'Hello Medicina'],
    'Inventario': ['inventario', 'Organizar es mi vida']
}


class User(UserMixin):

    def __init__(self, id_user):
        self.user_id = id_user
        self.active = False

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.user_id

    def get_rol(self):
        rol_0 = desencrypth(self.user_id)['rol']
        return rol_0

    def get_name_u(self):
        rol_0 = desencrypth(self.user_id)['rol']
        user_0 = desencrypth(self.user_id)['user']
        password_0 = desencrypth(self.user_id)['password']
        true_user = do_login(user_0, password_0, rol_0)['data'][0]

        return true_user['nombre']

    def important_data(self):
        rol_0 = desencrypth(self.user_id)['rol']
        user_0 = desencrypth(self.user_id)['user']
        password_0 = desencrypth(self.user_id)['password']
        true_user = do_login(user_0, password_0, rol_0)['data'][0]

        return true_user
