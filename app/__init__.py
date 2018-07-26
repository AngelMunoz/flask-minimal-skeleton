from flask import Flask, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')

CORS(app)
db = MongoEngine(app)
jwt = JWTManager(app)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not found', 'code': 'E_NOF'}), 404


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
