from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO, send, emit
from app.decorators import ws_jwt_required

app = Flask(__name__, static_folder='client')
app.config.from_object('config')

CORS(app)
db = MongoEngine(app)
jwt = JWTManager(app)
socketio = SocketIO(app)


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'message': 'Method Not Allowed', 'code': 'E_NOALW'}), 405


@app.errorhandler(500)
def server_error(error):
    return jsonify({'message': 'Server Error', 'code': 'E_SVRERR'}), 500


# Importing views
from app.auth.controller import auth
# register blueprints
app.register_blueprint(auth, url_prefix='/auth')


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    message_back = f'Hey Back There!'
    emit('message back', message_back)
    return message_back


@socketio.on('protected')
@ws_jwt_required
def handle_protected(message):
    print('received message: ' + message)
    message_back = f'Hey Back There!'
    emit('protected back', message_back)
    return message_back


@app.route('/')
def home():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('index.html')
