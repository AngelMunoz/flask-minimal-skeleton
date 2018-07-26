import functools
from flask_socketio import emit, disconnect
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError


def ws_jwt_required(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        try:
            verify_jwt_in_request()
            f(*args, **kwargs)
        except NoAuthorizationError as error:
            disconnect()
            return f'No Authorization Header Found {error}'
    return wrapped
