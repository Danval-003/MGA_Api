from flask import Flask, render_template, jsonify
from flask_cors import CORS
from extensions.unauthorized import unauthorized

from extensions.User_object import User
from routers.galeras import galery_bp
from routers.registerRoute import register_bp
from routers.lotes import lotes_bp
from routers.loginR import login_bp
from routers.creacion.crear_galera import cgalery_bp
from routers.creacion.crear_worker import worker_bp
from routers.asignacion.asignacion import asignation_bp
from routers.wxlote import wxlote_bp
from documentation.documentation import doc_bp
from extensions.login_manager import lm
from extensions.cache import app

# Se instancia para aceptar CORS
CORS(app)
# Crear una instancia de LoginManager:
login_manager = lm

login_manager.init_app(app)

# Se crea una clave secreta para encriptar el login
app.secret_key = 'ContenidoExclusivoMGA'

app.register_blueprint(register_bp)
app.register_blueprint(galery_bp)
app.register_blueprint(lotes_bp)
app.register_blueprint(doc_bp)
app.register_blueprint(login_bp)
app.register_blueprint(cgalery_bp)
app.register_blueprint(worker_bp)
app.register_blueprint(asignation_bp) 
app.register_blueprint(wxlote_bp)


@login_manager.request_loader
def load_user_from_request(request):
    # Obtiene el token de sesión de la cabecera "Authorization" de la solicitud HTTP
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    # Verifica el token de sesión y devuelve el usuario autenticado
    if auth_token:
        user = User(auth_token)
        if user:
            return user

    # Si el token no es válido, lanza una excepción Unauthorized (401)
    return unauthorized()


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login_manager.unauthorized_handler
def Unauthorized():
    return unauthorized()


@app.route('/')
def hello_world():
    return render_template('totalDoc.html')


@app.route('/hello')
def hel_world():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()
