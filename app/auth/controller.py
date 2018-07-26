from flask import Blueprint, request, jsonify
from app.models import User
from flask_jwt_extended import jwt_required, create_access_token,\
    get_jwt_identity
from mongoengine import ValidationError, NotUniqueError

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({"message": "Missing email parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400

    user = User.objects(email=email).first()
    if user == None:
        return jsonify({"message": "User not Found"}), 404

    if user.check_password(password):
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Incorrect Password"}), 200


@auth.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    if not request.json.get('password'):
        return jsonify({"message": "Missing password parameter"}), 400

    user = User(**request.json)
    user.set_password(request.json.get('password'))
    try:
        user.validate()
    except ValidationError as error:
        return jsonify(error.to_dict()), 400
    try:
        user.save()
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token), 200
    except NotUniqueError as error:
        return jsonify({
            'message': 'The email provided is already taken',
            'code': 'E_OCUPIED'
        }), 400

# Protect a view with jwt_required, which requires a valid access token
# in the request to access.


@auth.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
