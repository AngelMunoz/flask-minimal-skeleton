import os
# pulling from enviromental variable,
MONGODB_SETTINGS = {
    'host': os.environ.get('DATABASE_URL', "mongodb://localhost:27017/flaskmindb")
}
THREADS_PER_PAGE = 2
# secret key for cookies
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
JWT_SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
