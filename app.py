from flask import Flask
from flask_cors import CORS
from routers.galeras import galery_bp
from routers.registerRoute import register_bp

app = Flask(__name__)

# Se instancia para aceptar CORS
CORS(app)
app.register_blueprint(register_bp)
app.register_blueprint(galery_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
