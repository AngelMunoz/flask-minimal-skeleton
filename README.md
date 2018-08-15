[Flask]: http://flask.pocoo.org/
[blueprint]: http://flask.pocoo.org/docs/1.0/blueprints/
[JWT]: https://github.com/vimalloc/flask-jwt-extended
[previous project]: https://github.com/AngelMunoz/FlaskBlueprintsDemo
[auth]: https://github.com/AngelMunoz/flask-minimal-skeleton/blob/master/app/auth/controller.py
[MongoEngine]: http://docs.mongoengine.org/
[flask-mongoengine]: http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
[MongoDB]: https://www.mongodb.com/
[Aurelia]: https://aurelia.io/
[Bulma]: https://bulma.io/

# Minimal Flask Skeleton
This is a fairly small [Flask] skeleton that includes an [auth] [blueprint] with minimal details using [MongoEngine] (using [flask-mongoengine]) and [MongoDB] as a database engine

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

feel free to clone and add more stuff as your app grows.
if you feel I'm missing something, please send a pull request or raise an issue in github.
this repo was built from this [previous project].

to have the best experience developing this skeleton you should be using the following

- [Pipenv](https://github.com/pypa/pipenv)
- [VsCode](https://code.visualstudio.com/)
- [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

```
pipenv --three # creates a python 3 virtualenv
pipenv install
```

press <kbd>F5</kbd>

set a breakpoint and send a request

or just run
```
$ pipenv shell
(virtualenv) $ python app.py
```

and don't forget to update your custom variables in the `.env` file
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=mongodb://localhost:27017/vendutron
SECRET_KEY=2c997eed5386cde72187fe8e4f05505b0057c2530993214464824666c02081e0 # use your own
FLASK_DEBUG=True
DEBUG=True
```

if you intend to publish this repo else were remember to put `.env` file outside github I left it here for *completeness*

# Client
This sample also Includes an [Aurelia] Frontend, if you are not going to use it you may delete it.
the aurelia sample is made of the aurelia-cli webpack template, it spits out app.js and vendor.js
file to the `app/client` (it is taken as a static folder in `app/__init__.py`) and the `index.ejs`
to `app/templates/index.html`, so if you want to switch to another frontend you can just
spit the bundles and index files in those paths.

for the Client compilation just run `au build --watch` with your flask server running, you won't have
hot reload but an <kbd>F5</kbd> should reflect your changes.
I didn't include anything fancy besides [Bulma], so you still have to implement proper Auth state
management. While `sign up` and `log in` views work as intended, you still need to ensure
the `views` and `access_token` are correctly protected, this template should give you a start.