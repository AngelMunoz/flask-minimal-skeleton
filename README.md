[Flask]: http://flask.pocoo.org/
[blueprint]: http://flask.pocoo.org/docs/1.0/blueprints/
[JWT]: https://github.com/vimalloc/flask-jwt-extended
[previous project]: https://github.com/AngelMunoz/FlaskBlueprintsDemo
[auth]:

# Minimal Flask Skeleton
This is a fairly small [Flask] skeleton that includes an [auth] [blueprint] with minimal details

- Login
- SignUp
- Protected

It uses [JWT] authentication so it's already suited for RESTful API development
to create a new *module* (blueprint) create a directory, put an `__init__.py` inside, add your `controller.py` (tipically called `routes` in other flask apps) insert at least the following lines
```py
from flask import Blueprint
# <blueprint_name> = Blueprint('<blueprint_name>', __name__)
users = Blueprint('users', __name__)

@users.route('/')
def hello_users():
    """
    http://host:port/users
    (after you include your prefix in app/__init__.py)
    """
    return "Hello Users"
```
and inside `app/__init__.py` add the following lines
```py
from app.auth.controller import auth
from app.users.controller import users # this one
# register blueprints
app.register_blueprint(auth, url_prefix='/auth')
# http://host:port/users
app.register_blueprint(users, url_prefix='/users') # this one
```

feel free to clone and add more stuff as your app grows

if you feel I'm missing something, please send a pull request or raise an issue in github

this repo was built from this [previous project]